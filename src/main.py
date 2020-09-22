import argparse
import sys

import citycouncil.scraper
import geodistricts.scraper
import geonpus.scraper

def scraper(args):
    datasources = {
        "citycouncil": citycouncil.scraper,
        "geodistricts": geodistricts.scraper,
        "geonpus": geonpus.scraper
    }

    parser = argparse.ArgumentParser(description="Scrapes data from various Atlanta data sources.")
    parser.add_argument('--what', dest="what", required=True, choices=list(datasources.keys()), help="what to scrape")
    parser.add_argument('--out', dest="out", default=None, help="output file for scraped result")
    parsedArgs = parser.parse_args(args)

    datasources[parsedArgs.what].run(parsedArgs.out)

def server(args):
    parser = argparse.ArgumentParser(description="Serves scraped data from various Atlanta data sources.")
    parser.add_argument('--port', dest="what", type=int, default=8000, help="server port")
    print("server not implemented")

if len(sys.argv) < 2:
    print("Need a command argument.")
    sys.exit(2)

commands = {
    "scrape": scraper,
    "serve": server,
}

command = commands[sys.argv[1]]
command(sys.argv[2:])

