import pandas
import smtplib
import datetime as dt
import random

USER_EMAIL = "madhavdahal4@gmail.com"
PASSWORD = "qsak opry pnqq iyix"

now = dt.datetime.now()

birthdays = pandas.read_csv('birthdays.csv')
all_people = birthdays.to_dict('records')
today_birthdays = [
    item for item in all_people if item["month"] == now.month and item["day"] == now.day
]

try:
    for birthday in today_birthdays:
        random_number = random.randint(1, 3)
        with open(f'./letter_templates/letter_{random_number}.txt') as file:
            text = file.read().replace('[NAME]', birthday["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=USER_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=USER_EMAIL,
                to_addrs=birthday["email"],
                msg=f"Subject: Happy Birthday!\n\n{text}"
            )
except:
    print("today is no any birthday")

