import requests


class DataManager():
    # This class is responsible for talking to the Google Sheet.

    def __init__(self, rawdata):
        self.raw = rawdata

    def update(self):
        for count, item in enumerate(self.raw, 2):
            data = {
                "price": item
            }
            requests.put(url=f"https://api.sheety.co/95af271f4017f5445552c4362bef01b8/flightDeals/prices/{count}",
                         json=data)
