from utils.fetcher import Fetcher

def run():
    fetcher = Fetcher()
    fetcher.use("data/raw-geodistricts.json") #Use cached data.

    # Source: https://dcp-coaplangis.opendata.arcgis.com/datasets/npu
    url = "https://opendata.arcgis.com/datasets/91911cd123624a6b9b88cbf4266a2309_4.geojson"
    geojson, status_code = fetcher.fetch(url)
    if status_code != 200:
        print("Failed to contact", url, r.status_code)
        sys.exit(-1)
