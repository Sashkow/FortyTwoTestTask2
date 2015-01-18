"""
hello app views
"""
from django.shortcuts import render
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from apps.hello.models import Person, RequestData


def main_page(request):
    """
    A view that presents my name, surname, date of birth, bio, contacts
    on the main page.
    """
    user = User.objects.get(username='admin')
    person = Person.objects.get(user=user)
    return render(request, "hello/index.html", {'person': person})

def requests_page(request):
    """
    A view that shows first 10 http requests that are stored by middleware
    """
    shown_requests_count = 10
    template_name = 'hello/requests.html'
    requests = RequestData.objects.all()[:shown_requests_count]
    context = {'requests': requests}
    return render(request, template_name, context)

