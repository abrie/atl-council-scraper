import argparse
import sys

import citycouncil.scraper

def scraper(args):
    parser = argparse.ArgumentParser(description="Scrape the city council website for council member information.")
    parser.add_argument('--out', dest="out", default=None, help="output file for scraped result")
    parser.add_argument('--cached', dest="use_cache", default=False,const=True,action="store_const")
    parsedArgs = parser.parse_args(args)

    citycouncil.scraper.run(parsedArgs)

def help():
    print("atl-council-scraper scrapes the Atlanta City Council website.\n")
    print("Usage: atl-council-scraper scrape [arguments]\n")
    print("Arguments:\n")
    print("\t-h\t\tShow help")
    print("\t--out\t\tSpecify a file for scraped output")
    print("\t--cached\tScrape data from cached HTML, if available.")

def run():
    if len(sys.argv) < 2:
        help()
        sys.exit(2)

    commands = {
        "scrape": scraper,
    }

    command = sys.argv[1]

    if command in commands:
        commands[command](sys.argv[2:])
    else:
        print("Uknown command '%s'\n" % command)
        sys.exit(2)

if __name__ == '__main__':
    run()
