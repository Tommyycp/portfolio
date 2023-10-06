import requests
from datetime import datetime, timedelta

date_now = datetime.now()
today_date = date_now.strftime("%d/%m/%Y")

date_after_60 = date_now + timedelta(days=150)
date_after_60 = date_after_60.strftime("%d/%m/%Y")

TEQUILA_API = "uSRH1npGF8_m_a9ZHeFh021PhvG6N-H4"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, name):
        self.iata = None
        self.lowest_price = None
        self.departure_date = None
        self.city_name = name
        self.find_iata()
        self.find_cheapest()

    def find_iata(self):
        flight_search = requests.get(url="https://api.tequila.kiwi.com/locations/query",
                                     headers={"apikey": TEQUILA_API},
                                     params={"term": f"{self.city_name}"})
        data = flight_search.json()
        self.iata = data["locations"][0]["code"]

    def find_cheapest(self, origin="YVR", currency="HKD"):
        search_connection = requests.get(url="https://api.tequila.kiwi.com/v2/search", headers={"apikey": TEQUILA_API},
                                         params={
                                             "fly_from": origin,
                                             "fly_to": self.iata,
                                             "date_from": today_date,
                                             "date_to": date_after_60,
                                             "curr": currency,
                                             "max_stopers": 0,
                                         })
        data = search_connection.json()
        lowest = data['data'][0]
        self.lowest_price = lowest["price"]
        self.departure_date = lowest["local_departure"]
