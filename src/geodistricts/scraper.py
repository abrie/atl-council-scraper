from utils.fetcher import Fetcher
from utils.makefiledir import makefiledir
import json

# Source: https://dcp-coaplangis.opendata.arcgis.com/datasets/city-council-districts
URL = "https://opendata.arcgis.com/datasets/5ce01aea8d4046fe8659a8e25958c2bb_2.geojson"
CACHE = "data/raw-geodistricts.json"
FINISHED = "data/geodistricts.json"

def run(args):
    fetcher = Fetcher(cacheDest=CACHE)

    text, status_code = fetcher.fetch(URL, use_cache=args.use_cache)
    if status_code != 200:
        print("Failed to contact:", URL, r.status_code)
        sys.exit(2)

    fetcher.storeCache()

    geojson = json.loads(text)
    features = [feature for feature in geojson["features"]
                if feature["properties"]["GEOTYPE"] == "City Council District"]

    result = {"type":"FeatureCollection", "features":features}

    outfile = args.out if args.out != None else FINISHED
    makefiledir(outfile)

    with open(outfile,"w+") as f:
        f.write(json.dumps(result))
