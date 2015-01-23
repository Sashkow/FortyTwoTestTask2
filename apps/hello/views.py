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

import json

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
        # post = request.POST.copy()
        # post['user'] = person.user.pk
        form = PersonForm(request.POST, request.FILES, instance=person)
        if form.is_valid():
            form.save()
        else:
            return render(request, "hello/edit.html", 
            {'form': form, 'person': person})

        return HttpResponseRedirect(reverse('main'))
    else:
        form = PersonForm(instance=person)
    
    return render(request, "hello/edit.html", 
     {'form': form, 'person': person})

def edit_ajax(request):
    """
    a view that allows to save content of the main page without
    refreshing the page
    """
    usr_name = request.POST['name']
    person = Person.objects.get(user=request.user)
    person.name = usr_name
    person.save()


    response_data = {}
    response_data['result'] = 'success'
    response_data['name'] = person.name

    return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
        return HttpResponseRedirect(reverse('main'))
    else:
        form = AuthenticationForm()
    return render(request, 'hello/login.html', {'form': form})    