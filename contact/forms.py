from django import forms

class ContactForm(forms.Form):
	email = forms.EmailField(label="E-mail address:")
	message = forms.CharField(label="How can we help you?",widget=forms.Textarea)
	
	def save(self):
		from django.template import Context, loader
		from django.core.mail import send_mail
		from django.conf import settings
		
		t = loader.get_template('contact_form_email.phtml')
		send_mail(getattr(settings,'EMAIL_SUBJECT_PREFIX','[Match Strike] ')+'Contact form', t.render(Context({'form_data':self.cleaned_data})), None, ('info@matchstrike.net',))
