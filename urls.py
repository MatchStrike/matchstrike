from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^contact_us/', include('contact.urls')),
	(r'^more_news/', include('social.urls')),
	(r'^manage/', include(admin.site.urls)),
)

urlpatterns += patterns('',
	url(r'^$', direct_to_template, {'template': 'index.phtml'}, name='index'),
	url(r'^pricing/$', direct_to_template, {'template': 'pricing.phtml'}, name='pricing'),
	url(r'^refer_us/$', direct_to_template, {'template': 'referrals.phtml'}, name='refer_us'),
	url(r'^privacy/$', direct_to_template, {'template': 'privacy.phtml'}, name='privacy'),
	url(r'^work/$', direct_to_template, {'template': 'work.phtml'}, name='work'),
)

# If we're debugging, expose the static assets, 404, and 500 error pages so we can test them without a prod setup:
if getattr(settings, 'DEBUG', False):
	urlpatterns += patterns('',
		(r'^assets/(?P<path>.*)$', 'django.views.static.serve', {'document_root':getattr(settings,'MEDIA_ROOT')}),
		url(r'^404.html$', direct_to_template, {'template': '404.html'}, name='404_debug'),
		url(r'^500.html$', direct_to_template, {'template': '500.html'}, name='500_debug'),
	)