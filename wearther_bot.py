import config
import requests
import tweepy
import tweet_generate
import random
import emoji

url = ("https://api.darksky.net/forecast/{}/" + config.melbourne_location + "?units=si".format(config.dark_sky))
data = requests.get(url).json()

#depending on the temperature and if it's gonna rain, print that message

class Temperature(Enum):
    cold = 15
    nice = 25
    chance_of_rain = 0.5

max_temp = data['daily']['data'][0]['temperatureHigh']
risk_of_rain = data['daily']['data'][0]['precipProbability']
summary = data['daily']['data'][0]['summary']

if (max_temp) < Temperature.cold and (risk_of_rain) > Temperature.chance_of_rain:
    message = random.choice(tweet_generate.cold_sfx) + ' ' + random.choice(tweet_generate.cold_word) +
    ' with a top of ' + str((round(max_temp))) + '°C and a ' + str((format(risk_of_rain, ".0%"))) +
    ' chance of rain, so ' + random.choice(tweet_generate.dress_warm) + ' and remember your umbrella!' +
    ' ' + random.choice(tweet_generate.emoji)

if (max_temp) < Temperature.cold and (riskOfRain) < Temperature.chance_of_rain:
    message = random.choice(tweet_generate.cold_sfx) + ' ' + random.choice(tweet_generate.cold_word) +
    ' with a top of ' + str((round(max_temp))) + '°C and a ' + str((format(risk_of_rain, ".0%"))) +
    ' chance of rain, so ' + random.choice(tweet_generate.dress_warm) + ' before you leave the house!' +
    ' ' + random.choice(tweet_generate.emoji)

if Temperature.cold < (max_temp) < Temperature.nice and (riskOfRain) < Temperature.chance_of_rain:
    message = random.choice(tweet_generate.neutral_sfx) + ' ' + random.choice(tweet_generate.today_weather) +
    str(summary) + ' A top of ' + str((round(max_temp))) + '°C and a ' + str((format(risk_of_rain, ".0%"))) +
    ' chance of rain, so ' + random.choice(tweet_generate.dress_neutral) + ' and ' +
    random.choice(tweet_generate.neutral_greeting) + ' ' + random.choice(tweet_generate.emoji)

if Temperature.cold < (max_temp) < Temperature.nice and (riskOfRain) > Temperature.chance_of_rain:
    message = random.choice(tweet_generate.neutral_sfx) + ' ' + random.choice(tweet_generate.today_weather) +
    str(summary) + ' A top of ' + str((round(max_temp))) + '°C and a ' + str((format(risk_of_rain, ".0%"))) +
    ' chance of rain, so ' + random.choice(tweet_generate.dress_neutral) + ' and remember your umbrella!' +
    ' ' + random.choice(tweet_generate.emoji)

if (max_temp) > Temperature.nice:
    message = random.choice(tweet_generate.hot_sfx) + ' ' + random.choice(tweet_generate.today_weather) +
    str(summary) + ' A top of ' + str((round(max_temp))) + '°C and a ' + str((format(risk_of_rain, ".0%"))) +
    ' chance of rain, so ' + random.choice(tweet_generate.dress_light) + ' and protect yourself from the sun!' +
    ' ' + random.choice(tweet_generate.emoji)

#setting up tweepy and twitter bot

account = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
account.set_access_token(config.access_token, config.access_secret)
bot = tweepy.API(account)

bot.update_status(message)
