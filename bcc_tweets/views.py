#!/usr/bin/env python
# encoding: utf-8

"""
Extract tweets
"""

__author__ = 'Aazim'


from django.shortcuts import render
from django.http import HttpResponse
import tweepy
import datetime
   

def get_tweets(request):
	#Setting up developer keys for Tweepy access to twitter
	consumer_key = "JhtqmGSeqYRvbVUMxjUfKH5IJ"
	consumer_secret = "6CAFqoBonJSDRiAmAuphCSOyk1Zb8KxM7IXyMHj5lUifCxu7J0"
	access_key = "1075441158459817984-3cpGkHbDUtPFyryezmDJ9FCcd1kryN"
	access_secret = "j1fHZcLDXCqRASK3UddEOKEZeQX87vif9z4v02rp7dkIb"
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	tweet_dic = []
	startDate = datetime.datetime(2018, 11, 1, 0, 0, 0)
	endDate = datetime.datetime(2018, 12, 30, 0, 0, 0)

	#Extracting tweets with handle @BCCI
	for tweets in tweepy.Cursor(api.search,q='@BCCI',count=3,lang="en").items():
		if tweets.created_at < endDate and tweets.created_at > startDate:
			try:
				tweet_dic.append(tweets)
			except:
				pass

	return render(request, 'bcc_tweets/index.html', {'data':tweet_dic})