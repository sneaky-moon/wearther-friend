import keys
import requests
import tweepy
import tweetGenerate
import random
import emoji

url = ("https://api.darksky.net/forecast/{}/-37.8136,144.9631?units=si".format(keys.dark_sky))
data = requests.get(url).json()

#depending on the temperature and if it's gonna rain, print that message

maxTemp = data['daily']['data'][0]['temperatureHigh']
riskOfRain = data['daily']['data'][0]['precipProbability']
summary = data['daily']['data'][0]['summary']

if (maxTemp) < 15 and (riskOfRain) > 0.5:
    message = random.choice(tweetGenerate.coldsfx) + ' ' + random.choice(tweetGenerate.coldword) + ' with a top of ' + str((round(maxTemp))) + '°C and a ' + str((format(riskOfRain, ".0%"))) + ' of rain, so ' + random.choice(tweetGenerate.dresswarm) + ' and remember your umbrella!' + ' ' + random.choice(tweetGenerate.emoji)

if (maxTemp) < 15 and (riskOfRain) < 0.5:
    message = random.choice(tweetGenerate.coldsfx) + ' ' + random.choice(tweetGenerate.coldword) + ' with a top of ' + str((round(maxTemp))) + '°C and a ' + str((format(riskOfRain, ".0%"))) + ' of rain, so ' + random.choice(tweetGenerate.dresswarm) + ' before you leave the house!' + ' ' + random.choice(tweetGenerate.emoji)

if 15 < (maxTemp) < 25 and (riskOfRain) < 0.5:
    message = random.choice(tweetGenerate.neutralsfx) + ' ' + random.choice(tweetGenerate.todayweather) + str(summary) + ' A top of ' + str((round(maxTemp))) + '°C and a ' + str((format(riskOfRain, ".0%"))) + ' of rain, so ' + random.choice(tweetGenerate.dressneutral) + ' and ' + random.choice(tweetGenerate.neutralgreeting) + ' ' + random.choice(tweetGenerate.emoji)

if 15 < (maxTemp) < 25 and (riskOfRain) > 0.5:
    message = random.choice(tweetGenerate.neutralsfx) + ' ' + random.choice(tweetGenerate.todayweather) + str(summary) + ' A top of ' + str((round(maxTemp))) + '°C and a ' + str((format(riskOfRain, ".0%"))) + ' of rain, so ' + random.choice(tweetGenerate.dressneutral) + ' and ' + ' and remember your umbrella!' + ' ' + random.choice(tweetGenerate.emoji)

if (maxTemp) > 25:
    message = random.choice(tweetGenerate.hotsfx) + ' ' + random.choice(tweetGenerate.todayweather) + str(summary) + ' A top of ' + str((round(maxTemp))) + '°C and a ' + str((format(riskOfRain, ".0%"))) + ' of rain, so ' + random.choice(tweetGenerate.dresslight) + ' and ' + 'protect yourself from the sun!' + ' ' + random.choice(tweetGenerate.emoji)

#setting up tweepy and twitter bot

account = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
account.set_access_token(keys.access_token, keys.access_secret)
bot = tweepy.API(account)

bot.update_status(message)
