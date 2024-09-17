import random
import smtplib
import datetime as dt

my_email = "pythoncodingpractice11@gmail.com"
password = "dqyxbelnhdr"

def random_quote():
    with open("quotes.txt","r") as quote_file:
        quotes = quote_file.readlines()
    quote = random.choice(quotes)
    return quote

def send_quote():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="aragul@gmail.com",msg=f"subject:Monday motivational quote \n\n{random_quote()}")

today = dt.datetime.now()
day_of_week = today.weekday() + 1

if day_of_week == 2:
    send_quote()
    print("Successfully sent the  Quote")
