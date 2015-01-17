from django import forms
from django.forms import ModelForm
from apps.hello.models import Person

class PersonForm(ModelForm):
    """
    ModelForm to edit :model:`Pesron` and partially
    :model:`auth.User` models' fields in
    """
    class Meta:
        model = Person
        exclude = ('user',)

    name = forms.CharField(max_length=30, required=False)
    surname = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(required=False)

    def __init__(self, *args, **kwargs):
        """
        override: loads initial :model:`auth.User` data to form fields
        """
        if 'instance' in kwargs:
            instance = kwargs['instance']
            initial = kwargs.get('initial', {})
            initial['name'] = instance.name
            initial['surname'] = instance.surname
            initial['email'] = instance.email
            kwargs['initial'] = initial
        super(PersonForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        """
        override: saves :model:`auth.User` data on form commit
        """
        instance = super(PersonForm, self).save(commit)

        user = instance.user
        user.first_name = self.cleaned_data['name']
        user.last_name = self.cleaned_data['surname']
        user.email = self.cleaned_data['email']
        user.save()
        return instance
