# ATL City Council Scraper

[Atlanta's City Council website](https://citycouncil.atlantaga.gov/) contains information about current city council members.

This app pulls that information into a machine readable JSON file.

For an example of scraped data, [see here](tests/testdata/scraped.json).

## Run CLI Container

`docker run abriedev/atl-council-scraper scrape`

## Run From Source

__Requires Python 3.8__

1. `make dependencies`
2. `make test`
3. `python3 -m app scrape`
