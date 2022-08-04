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

If you get "Cannot connect to the Docker daemon", 
install the Docker Toolbox, which includes the Docker Machine.
https://github.com/docker/machine/releases

## Build from source

__Requires Python 3.8__

Create a virtual environment (OSX / Linux / Windows):
`python3 -m venv venv`

OSX / Linux:
`source venv/bin/activate`

Windows:
`\venv\Scripts\activate.bat`

Running `make dependencies` will install BeautifulSoup4

1. `make dependencies`
2. `make test`
3. `python3 -m app scrape > scraped/atl-citycouncil.json`