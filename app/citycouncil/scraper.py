from bs4 import BeautifulSoup
from app.utils.fetcher import Fetcher
from app.utils.makefiledir import makefiledir
import json
import sys
import itertools
import argparse

URL = "https://citycouncil.atlantaga.gov"
CACHE = "data/raw-citycouncil.json"
FINISHED = "data/citycouncil.json"

def getAllCouncilMembers(fetcher, use_cache=False):
    text, status_code = fetcher.fetch(URL, use_cache=use_cache)
    if status_code != 200:
        print("Failed to contact", URL, r.status_code)
        sys.exit(2)

    soup = BeautifulSoup(text, 'html.parser')
    tab = soup.find(id="ColumnUserControl2")
    nav = tab.find("nav")
    ul = nav.find("ul")
    lis = ul.find_all("li", recursive=False)
    hrefs = [li.find("a")["href"] for li in lis]
    return hrefs


def buildContact(strings):
    sections = {"Office Location":[],
                "P":[],
                "F":[],
                "E":[],
                "Committee Assignments":[]}

    section = None

    for string in strings:
        if string in sections:
            section = sections[string]
        elif section != None:
            section.append(string)

    remapping = {"Office Location":"office",
                 "P":"phone",
                 "F":"fax",
                 "E":"email",
                 "Committee Assignments":"committees"}

    remapped = {remapping.get(k, k): v for k, v in sections.items() if k in remapping}

    return remapped

def extractStrings(p):
        strings = [string for string in p.strings]
        strings = [string.split(":") for string in strings]
        strings = list(itertools.chain(*strings))
        strings = [string.strip() for string in strings]
        strings = list(filter(lambda string: string != '', strings))
        return strings

def extractEmails(p):
        mailtos = [a["href"] for a in p.select('a[href^="mailto:"]')]
        emails = [a.replace("mailto:","") for a in mailtos]
        emails = [email.strip() for email in emails]
        emails = list(dict.fromkeys(emails))
        return emails

def getCouncilMember(fetcher, href, use_cache=False):
    text, status_code = fetcher.fetch(href, use_cache=use_cache)
    if status_code != 200:
        return {'href': href, 'error': r.status_code}

    soup = BeautifulSoup(text, 'html.parser')
    name = soup.find("h1", ["titlewidget-title"]).find("span").contents[0]
    district = soup.find("h2", ["titlewidget-subtitle"]).contents[0]
    aside = soup.find("aside")
    image = aside.find("div", ["image_widget"]).find("img")["src"]
    content = aside.find("div", ["content_area"])
    contact = buildContact(extractStrings(content))
    contact["email"] = extractEmails(content)

    return {'href': href,
            'name': name,
            'district': district,
            'image': image,
            'contact': contact}

def run(args):
    print(args)
    fetcher = Fetcher(cacheDest=CACHE)

    members = [getCouncilMember(fetcher, href, use_cache=args.use_cache)
               for href in getAllCouncilMembers(fetcher, use_cache=args.use_cache)]

    fetcher.storeCache()

    if args.out == None:
        print(json.dumps(members, indent=2))
    else:
        makefiledir(args.out)
        with open(args.out, 'w', encoding='utf8') as json_file:
            json.dump(members, json_file, ensure_ascii=False)
