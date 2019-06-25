import emoji

account = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
account.set_access_token(keys.access_token, keys.access_secret)
bot = tweepy.API(account)

message = "\N{grinning face}"

bot.update_status(message)
