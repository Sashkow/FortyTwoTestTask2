from django.shortcuts import render
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from apps.hello.models import Person


def main_page(request):
    user = User.objects.get(username='admin')
    person = Person.objects.get(user=user)
    return render(request, "hello/index.html", {'person': person})
