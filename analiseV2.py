#-*- coding: utf-8 -*-

#Use Translate-cli to translate

from textblob import TextBlob
import tweepy
import numpy as np
import sys
import goslate
import subprocess
import time

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

tweets = api.user_timeline("pirofucusol", count=100)

for tweet in tweets:
	try:
		frase = TextBlob(tweet.text)
		cmd = 'translate-cli -f pt -t en "' + str(frase) + '" -o'
		process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
		out, err = process.communicate()

		print ("-----------------------------------------------")
		print "Texto Original: " + str(frase)
		print "Texto Traduzido: " + str(out).split('\n')[0]
		print('Tweet: {0} - Sentimento: {1}'.format(tweet.text.encode('utf-8'), TextBlob(out).sentiment))
	except:
		print "Err"
