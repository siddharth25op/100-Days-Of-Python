
# import smtplib
# import datetime as dt
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


#
# parameters = {
#     "title": "naruto"
# }
# response = requests.get(url="https://animechan.xyz/api/random/anime", params=parameters)
# response.raise_for_status()
# quote = response.json()["quote"]
# quoteBy = response.json()["character"]
#
# TOKEN = "5811571371:AAFF1b79OOoOiTvGDOqQk0i9DQAryK02L_I"
#
# chat_id = "2074577712"
# url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text=<b>{quote}</b>&parse_mode=html"
# requests.get(url).json()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import random
import tweepy

TOKEN = "5811571371:AAFF1b79OOoOiTvGDOqQk0i9DQAryK02L_I"


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hello {update.effective_user.first_name}")


async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    quotes_file_path = "quotes.txt"
    with open(quotes_file_path, "r") as file:
        lines = file.readlines()
        data = random.choice(lines)
        lines.remove(data)
        await update.message.reply_text(
            parse_mode="html",
            text=f"Here is your quote {update.effective_user.first_name}\n\n<b>{data}</b>"
        )

    consumer_key = 'ZvJ5YNqbVcnXa8x6eFAgdQ1IP'
    consumer_secret = 'xy9BxMbz3kW5SzmJkheYr2XYlBDvm4LsRlolgehBy02e25pKcZ'
    access_token = '1432973972220506113-ZDDTlfN8nF18igo7CRXHpGbruqeyfg'
    access_token_secret = '2yBBPqeY9E2uzMEZeAT7gW9LeiyCzztlQjPeFA2h3gNSt'

    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    client.create_tweet(text=data)
    with open(quotes_file_path, "w") as file:
        file.writelines(lines)


async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    api = "33ade1a2eec14e65e6d4b87c92a0def8"

    if context.args:
        city = " ".join(context.args)
    else:
        await update.message.reply_text("Please provide the command with the city name in the format '/weather city_name'")
        return

    parameters = {
        "appid": api,
        "cnt": 4,
        "q": city,
        "units": "metric"
    }

    response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
    response.raise_for_status()
    data = response.json()

    will_rain = False
    for hour_data in data["list"]:
        condition = hour_data["weather"][0]["id"]
        if int(condition) < 700:
            will_rain = True

    if will_rain:
        temp = f"Temperature: {data['list'][0]['main']['temp']}°C"
        tempMin = f"Min Temperature: {data['list'][0]['main']['temp_min']}°C"
        tempMax = f"Max Temperature: {data['list'][0]['main']['temp_max']}°C"
        main = f"Main: {data['list'][0]['weather'][0]['main']}"
        description = f"Description: {data['list'][0]['weather'][0]['description']}"
        await update.message.reply_text(
            f"It's going to rain today in {city}. Bring an umbrella! ☔\n\n{temp}\n{tempMin}\n{tempMax}\n{main}\n{description}"
        )
    else:
        temp = f"Temperature: {data['list'][0]['main']['temp']}°C"
        tempMin = f"Min Temperature: {data['list'][0]['main']['temp_min']}°C"
        tempMax = f"Max Temperature: {data['list'][0]['main']['temp_max']}°C"
        main = f"Main: {data['list'][0]['weather'][0]['main']}"
        description = f"Description: {data['list'][0]['weather'][0]['description']}"
        await update.message.reply_text(
            f"The weather is fine today in {city}.\n\n{temp}\n{tempMin}\n{tempMax}\n{main}\n{description}"
        )


async def tt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    image_path = 'https://cdn.discordapp.com/attachments/1121455362311196814/1186640065712099338/image.png?ex=6593fbae&is=658186ae&hm=bf28f08663baf17d337531ac436deb595fba3248c699de96f7c2fa46faec4b15&'
    await update.message.reply_photo(image_path)


async def syllabus(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file_path = "https://cdn.discordapp.com/attachments/1121455362311196814/1186642633150431314/Syllabus_6h_Sem.pdf?ex=6593fe12&is=65818912&hm=ec08485d76bb0a1455d85846ca09ff9080e1cf9949ae98c55d86e52f759d849b&"
    await update.message.reply_document(file_path)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("quote", quote))
app.add_handler(CommandHandler("weather", weather))
app.add_handler(CommandHandler("tt", tt))
app.add_handler(CommandHandler("sb", syllabus))

app.run_polling()

# import tweepy
# t_client_id="RDZFZ3BoV3ZVSXhCSTFuR0xVM0k6MTpjaQ"
# t_client_secret="O7LVbtklOCo62EIDC7gZWEvp3EvWBsVfSHASvoY_XBGvoxx7RB"
#
#
# # Set your Twitter API credentials
# consumer_key = 'ZvJ5YNqbVcnXa8x6eFAgdQ1IP'
# consumer_secret = 'xy9BxMbz3kW5SzmJkheYr2XYlBDvm4LsRlolgehBy02e25pKcZ'
# access_token = '1432973972220506113-ZDDTlfN8nF18igo7CRXHpGbruqeyfg'
# access_token_secret = '2yBBPqeY9E2uzMEZeAT7gW9LeiyCzztlQjPeFA2h3gNSt'
#
# # Authenticate with Twitter
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)
#
#
# # Tweet function
# def tweet(message):
#     try:
#         api.update_status(status=message)
#         print("Tweet posted successfully.")
#     except tweepy.errors.TweepyException as e:
#         print(f"Error posting tweet: {e}")
#
#
# # Example usage
# if __name__ == "__main__":
#     tweet("Something")

#
# # Set your Twitter API v2 credentials
# BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAADa6fwEAAAAAmOwhMf%2FwC7SXHvNqoUorrxlYASs%3DLXPPzjGO7vhlZiwY6V2HincTPlmN17igz4avJ1uT9JVfBpTK8V'
# consumer_key = 'ZvJ5YNqbVcnXa8x6eFAgdQ1IP'
# consumer_secret = 'xy9BxMbz3kW5SzmJkheYr2XYlBDvm4LsRlolgehBy02e25pKcZ'
# access_token = '1432973972220506113-ZDDTlfN8nF18igo7CRXHpGbruqeyfg'
# access_token_secret = '2yBBPqeY9E2uzMEZeAT7gW9LeiyCzztlQjPeFA2h3gNSt'
# # Authenticate with Twitter
# auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
# api = tweepy.API(auth)
#
#
# # Tweet function
# def tweet(message):
#     try:
#         api.update_status(status=message)
#         print("Tweet posted successfully.")
#     except tweepy.errors.TweepyException as e:
#         print(f"Error posting tweet: {e}")
#
#
# tweet("Something")

# from twython import Twython
#
#
# twitter = Twython(
#     consumer_key,
#     consumer_secret,
#     access_token,
#     access_token_secret
# )
#
# message = "Hello world!"
# twitter.update_status(status=message)
