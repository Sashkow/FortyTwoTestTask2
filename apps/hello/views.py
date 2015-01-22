"""
hello app views
"""
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User
from apps.hello.models import Person, RequestData

from apps.hello.forms import PersonForm

from apps.hello.utils import get_person_or_admin

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import authenticate
from django.contrib import auth

def main(request):
    """
    A view that presents my name, surname, date of birth, bio, contacts
    on the main page.
    """
    person = get_person_or_admin(request)

    # if hasattr(person.ava,'url'):
    #     ava_url = person.ava.url
    # else:
    #     ava_url = ""
    # print person.ava.thumbnail.url
    return render(request, "hello/index.html", \
     {'person': person})

def requests(request):
    """
    A view that shows first 10 http requests that are stored by middleware
    """
    shown_requests_count = 10
    template_name = 'hello/requests.html'
    requests = RequestData.objects.all()[:shown_requests_count]
    context = {'requests': requests}
    return render(request, template_name, context)

def edit(request):
    """
    A view that allows to edit content from 'main' view
    """

    person = get_person_or_admin(request)
    
    if request.method == 'POST':

        form = PersonForm(request.POST, request.FILES, instance=person)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('main'))
    else:
        form = PersonForm(instance=person)
    
    
    return render(request, "hello/edit.html", 
     {'form': form, 'person': person})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
        return HttpResponseRedirect(reverse('main'))
    else:
        form = AuthenticationForm()
    return render(request, 'hello/login.html', {'form': form})    