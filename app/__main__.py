import sys

import app.citycouncil.scraper
import app.arguments

if __name__ == '__main__':
    args = app.arguments.parse(sys.argv[1:])

    commands = {
        "scrape": app.citycouncil.scraper.run,
    }

    commands[args.command](args)
