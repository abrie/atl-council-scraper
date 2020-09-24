# -*- coding: utf-8 -*-

import os
import json
import unittest
import app.citycouncil.scraper
import app.arguments
from app.utils.fetcher import Fetcher

def loadtestdata(filename):
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testdata", filename)
    return open(filepath,"r")

class IntegrationTest(unittest.TestCase):

    def testAgainstCache(self):
        expectedTestDataFile = loadtestdata("scraped.json")
        expected = json.loads(expectedTestDataFile.read())
        expectedTestDataFile.close()
        expected.sort(key=lambda o: o["href"])

        cached = loadtestdata("cached.json")
        fetcher = Fetcher(use_cache=cached, store_cache=None)
        got = app.citycouncil.scraper.scrape(fetcher)
        got.sort(key=lambda o: o["href"])

        self.assertEqual(len(expected), len(got))

        for (a,b) in zip(expected, got):
            self.assertDictEqual(a, b)

if __name__ == '__main__':
    unittest.main()
