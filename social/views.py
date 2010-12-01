from django.template import RequestContext
from django import http
from django.utils import simplejson
from django.template import loader
from syncr.delicious.models import Bookmark
from syncr.twitter.models import Tweet

def get_more_news(request, timestamp):
	from django.utils import simplejson
	from social.models import SyncedItems
	from syncr.delicious.models import Bookmark
	from syncr.twitter.models import Tweet
	from datetime import datetime
	
	# Verify that timestamp is a valid unix time stamp
	try:
		timestamp = datetime.fromtimestamp(int(timestamp))
	except:
		json_response = {'news':''}
		status = simplejson.dumps(json_response)
		return http.HttpResponse(status, mimetype="application/json")
	
	syncr = SyncedItems()
	recent_events = []
	for event in syncr.get_latest(0,15,timestamp):
		if isinstance(event, Tweet):
			recent_events.append(loader.render_to_string("events.phtml",{"recent_events":(('tweet',event),)},context_instance=RequestContext(request)))
		elif isinstance(event, Bookmark):
			recent_events.append(loader.render_to_string("events.phtml",{"recent_events":(('bookmark',event),)},context_instance=RequestContext(request)))
		
	json_response ={'news':recent_events}
	status = simplejson.dumps(json_response)
	return http.HttpResponse(status, mimetype="application/json")