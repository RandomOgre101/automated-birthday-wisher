import smtplib, random, datetime as dt, pandas as pd

my_email = "EMAIL"
password = "PASSWORD"


df = pd.read_csv("birthdays.csv")
bday_list = df.to_dict(orient="records")
l1 = 'letter_1.txt'
l2 = 'letter_2.txt'
l3 = 'letter_3.txt'
letter_list = [l1,l2,l3]


now = dt.datetime.now()
today_day = now.day
today_month = now.month

for bday in bday_list:
    if bday["day"] == today_day and bday["month"] == today_month:
        letter = random.choice(letter_list)
        to_send = ""
        with open(f"{letter}") as file:
            letter_contents = file.read()
            to_send += letter_contents.replace("[NAME]", bday["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=bday["email"], msg=f"Subject: Happy Birthday {bday['name']}!\n\n{to_send}")

to_send = ""




