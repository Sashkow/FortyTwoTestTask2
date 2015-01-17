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
    pickled_request = models.TextField(default="Empty")
    pub_date = models.DateTimeField('date published', default=timezone.now())

    # def __str__(self):
    #     return str(self.pub_date) + " " + \
    #      str(self.pickled_request)[:100] + "..."

