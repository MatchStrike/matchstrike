from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('contact.views',
	url(r'^$', 'contact', name="contact_us"),
)

urlpatterns += patterns('',
	url(r'thanks/$', direct_to_template, {'template': 'thanks.phtml'}, name='contact_thanks'),
)