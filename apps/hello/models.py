"""
app hello models
"""
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Person(models.Model):
    """
    Model to store my name, surname, date of birth, bio,
    contacts in access to :model:`auth.User` fields provided via properties
    """
    user = models.OneToOneField(User)

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


class RequestData(models.Model):
    class Meta:
        """
        RequestModelMeta class
        """
        ordering = ('-pub_date', )

    path = models.CharField(max_length=2000, null=True, blank=True)
    method = models.CharField(max_length=4, null=True, blank=True)
    args = models.TextField(null=True, blank=True)
    username = models.CharField(max_length=30, null=True, blank=True)
    pub_date = models.DateTimeField('date published', default=timezone.now())

    def __str__(self):
        return " ".join([str(field.name) + ":" + \
         str(getattr(self, field.name)) for field in self._meta.fields])
