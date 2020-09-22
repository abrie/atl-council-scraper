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
    parser.add_argument('--cached', dest="use_cache", default=False,const=True,action="store_const")
    parsedArgs = parser.parse_args(args)

    datasources[parsedArgs.what].run(parsedArgs)

def server(args):
    parser = argparse.ArgumentParser(description="Serves scraped data from various Atlanta data sources.")
    parser.add_argument('--port', dest="what", type=int, default=8000, help="server port")
    print("server not implemented")

def run():
    if len(sys.argv) < 2:
        print("atl-city-scraper")
        print("\nScrape and serve city information from various Atlanta resources")
        sys.exit(2)

    commands = {
        "scrape": scraper,
        "serve": server,
    }

    command = commands[sys.argv[1]]
    command(sys.argv[2:])

if __name__ == '__main__':
    run()
