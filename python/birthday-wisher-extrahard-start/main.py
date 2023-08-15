import datetime as dt
import smtplib
import pandas as pd
import random as r

now = dt.datetime.now()
month = now.month
day = now.day


def add_to_csv(name, email, year, month, day):
    data = pd.read_csv("./birthdays.csv")
    dict_data = {"name": [name], "email": [email], "year": [year], "month": [month], "day": [day], }
    dict_data = pd.DataFrame.from_dict(dict_data)
    dict_data.to_csv(path_or_buf="./birthdays.csv", mode="a", header=False, index=False)


def send_email(name, email_address):
    with open(file=f"./letter_templates/letter_{r.randint(1, 3)}.txt", mode="r") as file:
        file = file.read()
        message = file.replace("[NAME]", name)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login("tommyycp.rommates@gmail.com", "nuaojbfudcahvesy")
        connection.sendmail(from_addr="tommyycp.rommates@gmail.com", to_addrs=email_address, msg=message)


df = pd.read_csv("./birthdays.csv")
rslt_df = df[(df['month'] == month) & (df['day'] == day)]
if len(rslt_df) > 0:
    for i, d in rslt_df.iterrows():
        receiver = d['name']
        email = d['email']
        send_email(receiver, email)
        print(f"email sent to {receiver} at {email}")
else:
    print("Today is no one's birthday")

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
