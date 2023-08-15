import requests

PARA = dict(lat=22.3193, lng=114.1694, formatted=0)
response = requests.get(url="https://api.sunrise-sunset.org/json", params=PARA)
response = response.json()

sunrise = response["results"]["sunrise"]
sunset = response["results"]["sunset"]

sunrise = sunrise.split("T")[1].split("+")[0].split(":")
sunset = sunset.split("T")[1].split("+")[0].split(":")

sunrise_hour = int(sunrise[0]) + 7
sunset_hour = int(sunset[0]) + 7

if sunrise_hour >= 24:
    sunrise_hour = sunrise_hour - 24
sunrise[0] = f"{sunrise_hour}"
sunset[0] = f"{sunset_hour}"


