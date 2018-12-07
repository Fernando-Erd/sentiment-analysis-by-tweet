#-*- coding: utf-8 -*-
from textblob import TextBlob
import tweepy
import numpy as np
import sys
import goslate


#USE GOSLATE TO TRANSLATE

gs = goslate.Goslate()

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

tweets = api.user_timeline("pirofucusol")

for tweet in tweets:
	frase = TextBlob(tweet.text)
	print frase
	if frase.detect_language() != 'en':
		try:
			traducao = gs.translate(frase.translate(to='en')).decode('utf-8', 'ignore')
			print('Tweet: {0} - Sentimento: {1}'.format(tweet.text.encode('utf-8'), traducao.sentiment))
		except:
			print "Deu ruim"
	else:
		print frase
		print('Tweet: {0} - Sentimento: {1}'.format(tweet.text.encode('utf-8'), frase.sentiment))
