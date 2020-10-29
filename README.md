# ATL City Council Scraper

[Atlanta's City Council website](https://citycouncil.atlantaga.gov/) is the authoritative source of city council information.

This app scrapes the information into JSON format.

Scraping is done daily via Github Actions; which updates this repo with [the most recent data](scraped/atl-citycouncil.json).

If you prefer to run the scraper yourself, then you have two options:

## Run CLI Container

`docker run abriedev/atl-council-scraper scrape`

## Run From Source

__Requires Python 3.8__

1. `make dependencies`
2. `make test`
3. `python3 -m app scrape`
