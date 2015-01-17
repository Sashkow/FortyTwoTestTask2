from django.contrib import admin
from apps.hello.models import Person
from apps.hello.forms import PersonForm


class PersonAdmin(admin.ModelAdmin):
    """
    overriden :model:`hello.Person` ModelAdmin class show some
    :model:`auth.User`'s fields in context of :model:`hello.Person`'s
    admin change form
    """

    list_display = ('user', 'name', 'surname', 'birth_date', \
     'bio', 'email', 'jabber', 'skype', 'contacts')
    fields = ['name', 'surname', 'birth_date', \
     'bio', 'email', 'jabber', 'skype', 'contacts']

    form = PersonForm


admin.site.register(Person, PersonAdmin)
