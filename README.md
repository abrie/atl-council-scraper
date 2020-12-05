# ATL City Council Scraper

https://citycouncil.atlantaga.gov/ is the authoritative source for Atlanta City Council information.

This repository scrapes council member info into JSON for consumption by apps and APIs.

Scraping is done at 11am daily via Github Actions using the script in [.github/workflows/run-scraper.yml](.github/workflows/run-scraper.yml). Neat technique.<sup>[1](https://simonwillison.net/2020/Oct/9/git-scraping/)</sup>

Get the most recent [scraped data here](scraped/atl-citycouncil.json).

For self-hosting you have two options:

## Run in a container

`docker run abriedev/atl-council-scraper scrape`

Save output to a .json file in your root folder

`docker run abriedev/atl-council-scraper scrape > name-of-output-file.json`

## Build from source

__Requires Python 3.8__

1. `make dependencies`
2. `make test`
3. `python3 -m app scrape`
