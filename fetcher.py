import requests
import json
import sys
import pathlib

class Fetcher:
    def __init__(self):
        self.use_cached = False
        self.pages = {}

    def fetch(self, url):
        if self.use_cached:
            print("Use cached url:", url)
            cached = self.pages[url]
            return cached["text"], cached["status"]
        else:
            print("Fetching url:", url)
            r = requests.get(url)
            self.pages[url] = {"text":r.text, "status":r.status_code}
            return r.text, r.status_code

    def use(self, path):
        file = pathlib.Path(path)
        if file.exists():
            with open(file, "r") as f:
                self.pages = json.loads(f.read())
                self.use_cached = True

    def save(self, path):
        with open(path, "w+") as f:
            f.write(json.dumps(self.pages))

