from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm


def contact_page(request):
	form = ContactForm()
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			message.add_message(request, message,INFO, 'Submitted.')
			return redirect('contact')
	context = {
		'form' : form
	}
	return render(request, 'contact/contact.html', context)

