import keys
import requests
import tweepy

url = ("https://api.darksky.net/forecast/{}/-37.8136,144.9631?units=si".format(keys.dark_sky))
data = requests.get(url).json()

#depending on the temperature and if it's gonna rain, print that message

maxTemp = data['daily']['data'][0]['temperatureHigh']
riskOfRain = data['daily']['data'][0]['precipProbability']

#if maxTemp is lower than 15 degrees and more than 50% chance of rain
if(maxTemp) < 15 and (riskOfRain) > 0.5:
    message = "Brrrr! It's a cold one today at a top of " + str((round(maxTemp))) + "°C with a " + str((format(riskOfRain, ".0%"))) + " of rain, so dress warmly and remember your umbrella!"

#if maxTemp is lower than 15 degrees and less than 50% chance of rain
if(maxTemp) < 15 and (riskOfRain) < 0.5:
    message = "Good morning! It's gonna be a top of " + str((round(maxTemp))) + "°C today with a " + str((format(riskOfRain, ".0%"))) + " of rain, so maybe chuck on a coat before you leave the house!"


#to expand on the printing of messages, should do like a randomiser bot Ai thing?
#setting up tweepy and twitter bot

account = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
account.set_access_token(keys.access_token, keys.access_secret)
bot = tweepy.API(account)

bot.update_status(message)
