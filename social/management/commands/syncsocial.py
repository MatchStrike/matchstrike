from sys import exc_info

import tweepy

from django.core.management.base import BaseCommand
from syncr.twitter.models import Tweet
from syncr.twitter.models import TwitterUser
from syncr.app.delicious import DeliciousSyncr
from django.conf import settings


class Command(BaseCommand):
	def handle(self, *args, **options):
		# Get tweets
		for user in getattr(settings,'TWITTER_USERS',):
			try: 
				print "Attempting to sync Twitter user data for '%s'..." % (user['username'],)
				# Create Authenticated API Instance
				auth = tweepy.OAuthHandler(user['consumer_key'], user['consumer_secret'])
				auth.set_access_token(user['oauth_token'], user['oauth_secret'])
				twt = tweepy.API(auth)
				
				# Get last tweet
				try:
					last_tweet = Tweet.objects.all().order_by('-pub_time')[0].twitter_id
				except:
					print "No old tweets detected in the database. Importing all tweets: %s %s "% (exc_info()[0], exc_info()[1])
					last_tweet = None
				
				rate_limit_status = twt.rate_limit_status()
				tweets_inserted = 0
				if rate_limit_status.get('remaining_hits', 0) > 10:
					for x in tweepy.Cursor(twt.user_timeline, since_id=last_tweet).items():
						tweets_inserted = tweets_inserted + 1
						save_tweet(x)
				if rate_limit_status.get('remaining_hits', 0) > 10:
					for x in tweepy.Cursor(twt.retweeted_by_me, since_id=last_tweet).items():
						tweets_inserted = tweets_inserted + 1
						save_tweet(x)
				print "Success! %s tweets saved." % tweets_inserted
			except:
				print "An error occured while syncing Twitter data for '%s': %s %s" % (user['username'],exc_info()[0], exc_info()[1])
				print "Moving on..."
			print ""

def get_tweet_user(tweet):
	try:
		user = TwitterUser.objects.get(screen_name=tweet.user.screen_name)
	except:
		user = TwitterUser()
	
		user.screen_name = tweet.user.screen_name
		user.description = tweet.user.description
		user.location = tweet.user.location
		user.name = tweet.user.name
		user.thumbnail_url = tweet.user.profile_image_url
	
		user.save()
	
	return user

def save_tweet(tweet):
	new_tweet = Tweet()
	
	new_tweet.twitter_id = tweet.id
	if getattr(tweet, 'retweeted_status', False):
		new_tweet.pub_time = tweet.retweeted_status.created_at
		new_tweet.user = get_tweet_user(tweet.retweeted_status)
		new_tweet.text = tweet.retweeted_status.text
	else:
		new_tweet.pub_time = tweet.created_at
		new_tweet.user = get_tweet_user(tweet)
		new_tweet.text = tweet.text
	
	new_tweet.save()