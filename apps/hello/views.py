"""
hello app views
"""
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User
from apps.hello.models import Person, RequestData

from apps.hello.forms import PersonForm


def main(request):
    """
    A view that presents my name, surname, date of birth, bio, contacts
    on the main page.
    """
    person = Person.objects.get(user__username='admin')
    return render(request, "hello/index.html", {'person': person})

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
    person = Person.objects.get(user__username='admin')
    # if request.method == 'POST':
    #     form = PersonForm(instance=person, data=request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return HttpResponseRedirect(reverse('main'))
    # else:
    form = PersonForm(instance=person)

    return render(request, "hello/edit.html", {'form': form})
    


