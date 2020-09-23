import argparse
import sys

import app.citycouncil.scraper
import app.arguments

if __name__ == '__main__':
    args = app.arguments.parse(sys.argv)

    commands = {
        "scrape": app.citycouncil.scraper.run,
    }

    commands[args.command](args)

