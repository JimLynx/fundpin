from django.shortcuts import render, redirect
from projects.models import Project
from blog.models import Post

from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

from .forms import ContactForm


def index(request):
    """ return index page """

    projects = Project.objects.all()
    blog = Post.objects.all()

    context = {
        'projects': projects,
        'blogs': blog
    }

    return render(request, 'home/index.html', context)


def contact(request):
    """
    A view to return the contact form page & email functionality
    """
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email,
                          [settings.DEFAULT_FROM_EMAIL])
            except BadHeaderError:
                return HttpResponse('Invalid header found!')
            messages.success(request, (
                f'Thank you for contacting FundPIN, '
                ' your message has been sent! '
                'We will respond to you as soon as possible.'))
            return redirect('home')

    template = 'home/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
