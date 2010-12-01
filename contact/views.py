from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse

def contact(request):
	from contact.forms import ContactForm
	
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('contact_thanks'))
	else:
		form = ContactForm()
		
	return render_to_response('contact.phtml',{'form':form},context_instance=RequestContext(request))