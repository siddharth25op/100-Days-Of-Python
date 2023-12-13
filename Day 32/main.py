# import random
# import smtplib
# import datetime as dt
#
# email = ""
# password = ""
#
# now = dt.datetime.now()
# weekday = now.weekday()
# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#
# with open("quotes.txt") as file:
#     quote = random.choice(file.readlines())
#
#
# def sendquote():
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=email, password=password)
#         connection.sendmail(
#             from_addr=email,
#             to_addrs="",
#             msg=f"Subject:{days[weekday]} Motivation\n\n{quote}"
#         )
#
#
# sendquote()
