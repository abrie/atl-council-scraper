import requests
import json
import sys


class Fetcher:
    def __init__(self, use_cache=None, store_cache=None):
        self.use_cache = False
        self.store_cache = None
        if use_cache:
            self.pages = json.loads(use_cache.read())
            use_cache.close()
            self.use_cache = True
        if store_cache:
            self.pages = {}
            self.store_cache = store_cache

    def fetch(self, url, use_cache=False):
        if self.use_cache:
            print("Using cached url:", url, file=sys.stderr)
            cached = self.pages[url]
            return cached["text"], cached["status"]
        else:
            print("Fetching url:", url, file=sys.stderr)
            r = requests.get(url)
            if self.store_cache:
                self.pages[url] = {
                    "text": r.text,
                    "status": r.status_code
                }
            return r.text, r.status_code

    def storeCache(self):
        if self.store_cache:
            self.store_cache.write(json.dumps(self.pages))
            self.store_cache.close()
