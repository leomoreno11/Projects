#This program reads tweets made within a week and scans it to categorize as a positive or negative opinion.
#In the cryptocurrency world, the Fear vs Greed index is one way of analysing if an asset will increase or decrease.
#This program tries to do that index.

from os import truncate
from datetime import date, timedelta
from nltk.util import pr
import tweepy
import textblob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

#Dogecoin Analysis header
print('+_____________________________________________________________________________________+')
print('|  _____                             _                              _           _     |')
print('| |  __ \                           (_)           /\               | |         (_)    |')
print('| | |  | | ___   __ _  ___  ___ ___  _ _ __      /  \   _ __   __ _| |_   _ ___ _ ___ |')
print('| | |  | |/ _ \ / _  |/ _ \/ __/ _ \| |  _ \    / /\ \ |  _ \ / _  | | | | / __| / __||')
print('| | |__| | (_) | (_| |  __/ (_| (_) | | | | |  / ____ \| | | | (_| | | |_| \__ \ \__ \|')
print('| |_____/ \___/ \__, |\___|\___\___/|_|_| |_| /_/    \_\_| |_|\__,_|_|\__, |___/_|___/|')
print('|                __/ |                                                 __/ |          |')
print('|               |___/                                                 |___/           |')
print('+_____________________________________________________________________________________+')
print('')
print('                                   ▄              ▄')
print('                                  ▌▒█           ▄▀▒▌')
print('                                  ▌▒▒█        ▄▀▒▒▒▐')
print('                                 ▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐')
print('                               ▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐')
print('                             ▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌')
print('                            ▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌')
print('                            ▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐')
print('                           ▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌')
print('                           ▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌')
print('                          ▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐')
print('                          ▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌')
print('                          ▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐')
print('                           ▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌')
print('                           ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐')
print('                            ▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌')
print('                              ▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀')
print('                                ▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀')
print('                                   ▒▒▒▒▒▒▒▒▒▒▀▀')



#twitter keys order
# 1. API Key
# 2. API Secret Key
# 3. Access Token
# 4. Access secret Token

#Collects the parameters from a keys.txt file
#Create your own file with own parameters. Always include they in the order specified above
twitterkeys = open('keys.txt' , 'r').read().splitlines()
api_key =            twitterkeys [0]
secret_key =         twitterkeys [1]
access_token =       twitterkeys [2]
accessSecret_token = twitterkeys [3]
print("\n>> Complete key collection")
print('Api:          ', api_key)
print('Secret Key:   ', secret_key)
print('Access Token: ', access_token)
print('Secret Access Token: ', accessSecret_token)
print('_' * 70)

auth = tweepy.OAuthHandler(api_key,secret_key)
auth.set_access_token(access_token, accessSecret_token)
api = tweepy.API(auth)


#Definition of dates
today = date.today()
weekago  = date.today() - timedelta(days=7) #subtracs 7 days (one week) from the present date

doge = 'Dogecoin'
search = f'#{doge} -filter:retweets' #defines the search term ('q' parameter at tweet_cursor)
# filtes for retweets, maintaing the search minimal as possible and also focusing in the data that matters

tweet_cursor = tweepy.Cursor(api.search, q=search, lang='en', until = today, since=weekago, tweet_mode='extended').items(1000)
# tweet_mode='extended' :  the text attribute of Status objects returned by tweepy.API methods is replaced
# by a full_text attribute, which contains the entire untruncated text of the Tweet
# items define the quantity of tweets to be analysed

tweets = [tweet.full_text for tweet in tweet_cursor]
#list comprehenssion that gets each tweet from tweet_cursor and saves it into a list

#Converting the tweets into a dataframe utilizing the Pandas library
tweets_df = pd.DataFrame(tweets, columns=['Tweets'])

#Processing of cleaning the tweets for analysis
for _, row in tweets_df.iterrows():
    row['Tweets'] = re.sub('http\S+' , '', row['Tweets'])
    row['Tweets'] = re.sub('#\S+'    , '', row['Tweets'])
    row['Tweets'] = re.sub('@\S+'    , '', row['Tweets'])
    row['Tweets'] = re.sub('\\n'     , '', row['Tweets'])
#re.sub : Return the string obtained by replacing the leftmost nonNEGATIVEoverlapping occurrences of pattern
#in string by the replacement repl. If the pattern isn’t found, string is returned unchanged.

#Perform a sentiment analysis for all the individual Tweets and save a polarity score for them
tweets_df['Polarity']  = tweets_df['Tweets'].map(lambda tweet: textblob.TextBlob(tweet).sentiment.polarity)
tweets_df['Sentiment'] = tweets_df['Polarity'].map(lambda polarity: 'POSITIVE' if polarity > 0 else 'NEGATIVE')

#Counts the quantity of positive vs. negative tweets
positive = tweets_df[tweets_df.Sentiment == 'POSITIVE'].count()['Tweets']
negative = tweets_df[tweets_df.Sentiment == 'NEGATIVE'].count()['Tweets']

#Plot the graph utilizing matplotlib
plt.bar([0, 1], [positive, negative], label = ['Positive', 'Negative'], color=['blue', 'red'])
plt.title('Dogecoin Fear vs Greed this week\n' 
          + str(weekago) + ' - ' + str(today))#subtitle
plt.show()
