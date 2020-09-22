import requests
import json
import sys
import os

from utils.makefiledir import makefiledir

class Fetcher:
    def __init__(self, cacheDest=None):
        self.setCacheDest(cacheDest)

    def fetch(self, url, use_cache=False):
        if self.has_cache and use_cache:
            print("Using cached url:", url)
            cached = self.pages[url]
            return cached["text"], cached["status"]
        else:
            print("Fetching url:", url)
            r = requests.get(url)
            self.pages[url] = {"text":r.text, "status":r.status_code}
            return r.text, r.status_code

    def setCacheDest(self, path):
        self.cacheDest = path

        if self.cacheDest == None:
            self.pages = {}
            self.has_cache = False
        elif os.path.isfile(self.cacheDest):
            with open(self.cacheDest, "r") as f:
                self.pages = json.loads(f.read())
                self.has_cache = True
        else:
            self.has_cache = False
            self.pages = {}
            print("Warning: cache requested, but none exists.")

    def storeCache(self):
        if self.cacheDest != None:
            makefiledir(self.cacheDest)
            with open(self.cacheDest, "w+") as f:
                f.write(json.dumps(self.pages))

