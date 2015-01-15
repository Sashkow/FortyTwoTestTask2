from django.contrib import admin
from django import forms
from django.forms import ModelForm
from apps.hello.models import Person


# admin.site.register(Person)
class PersonForm(ModelForm):
    class Meta:
        model = Person
        exclude = ('user',)

    name = forms.CharField(max_length=30, required=False)
    surname = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required=False)

    def __init__(self, *args, **kwargs):
        if 'instance' in kwargs:
            instance = kwargs['instance']
            initial = kwargs.get('initial', {})
            initial['name'] = instance.name
            initial['surname'] = instance.surname
            initial['email'] = instance.email
            kwargs['initial'] = initial
        super(PersonForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(PersonForm, self).save(commit)

        user = instance.user
        user.first_name = self.cleaned_data['name']
        user.last_name = self.cleaned_data['surname']
        user.email = self.cleaned_data['email']
        user.save()
        return instance


class PersonAdmin(admin.ModelAdmin):

    list_display = ('user', 'name', 'surname', 'birth_date',
     'bio', 'email', 'jabber', 'skype', 'contacts')
    fields = ['name', 'surname', 'birth_date',
     'bio', 'email', 'jabber', 'skype', 'contacts']

    form = PersonForm


admin.site.register(Person, PersonAdmin)
