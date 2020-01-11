# gcloud functions deploy send_tweet --trigger-topic

import json
import tweepy
import time
import config


def get_first_retweet(api):
    # get our tweets
    tweets = api.user_timeline()

    # get the latest tweet
    latest_tweet = tweets[0]

    # get the tweet ID
    tweet_id = latest_tweet._json["id"]

    # tweet the tweet id
    retweets = api.retweets(tweet_id)

    # get the json data for the first user to retweet
    first = retweets[-1]._json

    # print(retweets[-1]._json["user"]["screen_name"])
    # print(json.dumps(first, indent=2) )

    # publish congratulations
    api.update_status("congrats to @" + first["user"]["screen_name"] +
                      " for being the first to retweet! stay lucky")




def send_tweet(event, context):

    api = tweepy.API()

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(config.CONSUMER_PUB,
                    config.CONSUMER_PRI)

    auth.set_access_token(config.ACCESS_PUB,
                          config.ACCESS_PRI)

    api = tweepy.API(auth)

    # Create a tweet
    api.update_status("hey everybody! it's testing time. make a wish!")

    # give up to x seconds for retweets to come in
    time.sleep(120)
    get_first_retweet(api)


