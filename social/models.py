from django.db import models

class SyncedItems():
	
	def __get_latest(self, start=0, limit=3, timestamp=None):
		from django.db import connection
		cursor = connection.cursor()
		if timestamp:
			cursor.execute("""
						select id, saved_date, 'bookmark' from delicious_bookmark where saved_date < %s
						UNION ALL
						select id, pub_time, 'tweet' from twitter_tweet where pub_time < %s
						ORDER BY 2 DESC	LIMIT %s, %s;""", [timestamp, timestamp, start, limit,])
		else:
			cursor.execute("""
							select id, saved_date, 'bookmark'
							from delicious_bookmark
							UNION ALL
							select id, pub_time, 'tweet'
							from twitter_tweet
							ORDER BY 2 DESC
							LIMIT %s, %s;
							""", [start, limit,])
		return cursor.fetchall()
	
	def get_latest(self, start=0, limit=3, timestamp = None):
		from syncr.delicious.models import Bookmark
		from syncr.twitter.models import Tweet
		
		ids = self.__get_latest(start, limit, timestamp)
		
		result = []
		for id in ids:
			if id[2] == 'tweet':
				result.append(Tweet.objects.get(pk=id[0]))
			if id[2] == 'bookmark':
				result.append(Bookmark.objects.get(pk=id[0]))
		
		return result
