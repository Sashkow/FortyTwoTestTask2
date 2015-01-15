
from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.OneToOneField(User)
    # name = models.OneToOneField(User.first_name)
    # surname = user.last_name
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    contacts = models.TextField(null=True, blank=True)
    jabber = models.CharField(max_length=50, null=True, blank=True)
    skype = models.CharField(max_length=50, null=True, blank=True)

    @property
    def name(self):
        return self.user.first_name
    @name.setter
    def name(self, value):
        self.user.first_name = value

    @property
    def surname(self):
        return self.user.last_name
    @surname.setter
    def surname(self, value):
        self.user.last_name = value

    @property
    def email(self):
        return self.user.email
    @email.setter
    def email(self, value):
        self.user.email = value

    def __str__(self):
        return " ".join([self.name, self.surname])
