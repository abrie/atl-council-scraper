from fetcher import Fetcher
import json

# Source: https://dcp-coaplangis.opendata.arcgis.com/datasets/city-council-districts
URL = "https://opendata.arcgis.com/datasets/5ce01aea8d4046fe8659a8e25958c2bb_2.geojson"
CACHE = "data/raw-geodistricts.json"
FINISHED = "data/geodistricts.json"

def run():
    fetcher = Fetcher()
    fetcher.use(CACHE) #Use cached data.

    text, status_code = fetcher.fetch(URL)
    if status_code != 200:
        print("Failed to contact", URL, r.status_code)
        sys.exit(-1)


    geojson = json.loads(text)
    features = [feature for feature in geojson["features"] if feature["properties"]["GEOTYPE"] == "City Council District"]

    result = {"type":"FeatureCollection", "features":features}
    with open(FINISHED,"w+") as f:
        f.write(json.dumps(result))

    fetcher.save(CACHE)

run()
