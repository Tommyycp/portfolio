import smtplib
import datetime as dt
import random as r

USERNAME = "tommyycp.rommates@gmail.com"
PASSWORD = "nuaojbfudcahvesy"
HOST = "smtp.gmail.com"
PORT = 587


def send_email(subject, message, recipient="yu152546983@gmail.com"):
    with smtplib.SMTP(host=HOST, port=PORT) as connection:
        connection.starttls()
        connection.login(user=USERNAME, password=PASSWORD)
        connection.sendmail(from_addr=USERNAME, to_addrs=recipient, msg=f"Subject:{subject}\n\n{message}")


# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# hour = now.hour
# minute = now.minute
# dotw = now.weekday()
#
# print(dotw)

with open("./quotes.txt", "r") as file:
    quotes = file.read()
    quotes = quotes.splitlines()

quote = r.choice(quotes)

now = dt.datetime.now()
if now.weekday() == 3:
    send_email("Your Daily Words of Affirmation", quote)
