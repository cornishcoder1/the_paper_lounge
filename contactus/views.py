from django.shortcuts import render

from django.views import View
from django.contrib import messages
from .forms import ContactForm


class Contact(View):
    """ View to allow sending of messages """
    def get(self, request, *args, **kwargs):

        return render(
            request,
            'contact.html',
            {
                'contact_form': ContactForm()
            }
        )

    def post(self, request, *args, **kwargs):

        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Thanks for your message!')

        else:
            contact_form = ContactForm()
            # messages.add_message(request, messages.WARNING,
            #                      'Message not sent. Please see ' +
            #                      '"Guidance on submitting messages."')

        return render(
            request,
            'contact.html',
            {
                'contact_form': ContactForm()
            }
        )
