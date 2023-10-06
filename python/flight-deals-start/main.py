# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
import data_manager
from flight_search import FlightSearch
from data_manager import DataManager
from pprint import pprint
from notification_manager import NotificationManager

TEQUILA_API = "uSRH1npGF8_m_a9ZHeFh021PhvG6N-H4"


# Establishing connection
connection = requests.get(url="https://api.sheety.co/95af271f4017f5445552c4362bef01b8/flightDeals/prices")

# Adding connection.json is a must for very api
response_json = connection.json()

sheet_data = response_json["prices"]

for i in sheet_data:
    new_city = FlightSearch(i['city'])
    i["iataCode"] = new_city.iata
    if i["lowestPrice"] > new_city.lowest_price:
        NotificationManager(new_city.city_name, new_city.departure_date, new_city.lowest_price)

# updater = DataManager(sheet_data)
# updater.update()


