import requests
from datetime import datetime
import smtplib
import time


def send_email(recipient_address, subject, content):
    USERNAME = "tommyycp.rommates@gmail.com"
    PASSWORD = "nuaojbfudcahvesy"
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as email_server:
        email_server.starttls()
        email_server.login(user=USERNAME, password=PASSWORD)
        email_server.sendmail(from_addr=USERNAME, to_addrs=recipient_address, msg=f"Subject:{subject} \n\n {content}")


iss = requests.get(url="http://api.open-notify.org/iss-now.json")
iss = iss.json()
iss_latitude = float(iss["iss_position"]["latitude"])
iss_longitude = float(iss["iss_position"]["longitude"])


def is_night_time(latitude=22.3193, longitude=114.1694):
    para = dict(lat=latitude, lng=longitude, formatted=0)
    sunset_sunrise = requests.get(url="https://api.sunrise-sunset.org/json", params=para)
    sunset_sunrise = sunset_sunrise.json()
    sunset_time = sunset_sunrise["results"]["sunset"].split("T")[1].split("+")[0].split(":")[0]
    sunset_minute = float(sunset_sunrise["results"]["sunset"].split("T")[1].split("+")[0].split(":")[1])
    sunset_hour = float(sunset_time)
    now = datetime.now()
    if sunset_hour < now.hour:
        return True
    elif sunset_hour == now.hour and sunset_minute < now.minute:
        return True
    else:
        return False


minute = 0
while True:
    if 17 < iss_latitude < 27 and 110 < iss_longitude < 120 and is_night_time():
        send_email("yuchingpanatwork@gmail.com", "LOOK UP THE SKY!", "An ISS station is now spottable.")
        break
    time.sleep(60)
    minute += 1
    if minute >= 1440:
        break
