import smtplib


# my_email = "pythoncodingpractice11@gmail.com"
# password = "dqyxbelnhuqlfndr"

# with smtplib.SMTP("smtp.gmail.com") as connection :
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#         to_addrs="aragul@gmail.com",
#         msg="subject:this is the title hackathon event invitation \n\n this the body of my email How are you")

import datetime as dt

now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()

date_of_birth = dt.datetime(day=11,month=9,year=2006)
print(date_of_birth)