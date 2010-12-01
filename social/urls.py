from django.conf.urls.defaults import *

urlpatterns = patterns('social.views',
	url(r'^(?P<timestamp>[0-9]*)/$', 'get_more_news', name="more_news"),
)
