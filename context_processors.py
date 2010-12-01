from django.conf import settings
from social.models import SyncedItems
from syncr.delicious.models import Bookmark
from syncr.twitter.models import Tweet

def default(request):
	syncr = SyncedItems()
	recent_events = []
	for event in syncr.get_latest(0,3):
		if isinstance(event, Tweet):
			recent_events.append(('tweet',event))
		elif isinstance(event, Bookmark):
			recent_events.append(('bookmark',event))
	return {'recent_events':recent_events}