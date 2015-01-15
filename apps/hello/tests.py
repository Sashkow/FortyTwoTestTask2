"""
hello app tests
"""
from django.test import TestCase

from django.core.urlresolvers import reverse
# from django.test import Client
from django.test.client import RequestFactory

from apps.hello.models import Person
from django.contrib.auth.models import User

from apps.hello.admin import PersonForm


class MainPageViewTestCase(TestCase):
    """
    tests for main-page view
    """
    fixtures = ['test_data.json']

    def setUp(self):
        pass

    def test_main_page_view_returns_200(self):
        """
        test main_page renders page successfully
        i. e. returns response with status code 200
        """
        response = self.client.get(reverse('main-page'))
        self.assertEquals(response.status_code, 200)

    def test_context_exist_and_correct(self):
        """
        test main_page view renders page with data taken from models
        """

        personfields_wishdict = {'name': 'Olexandr',
                                 'surname': 'Lykhenko',
                                 'email': 'lykhenko.olexandr@gmail.com',
                                 'birth_date': '1991-02-01',
                                 'bio': "Dnipropetrovsk",
                                 'contacts': 'linkedin',
                                 'jabber': 'sashko@42cc.co',
                                 'skype': 'sashkointelcore2duo',
                                }

        response = self.client.get(reverse('main-page'))
        self.assertTrue('person' in response.context)
        person = response.context['person']
        self.assertTrue(isinstance(person, Person))
        for name, value in personfields_wishdict.iteritems():
            self.assertTrue(hasattr(person, name))
            self.assertTrue(value in str(person.__getattribute__(name)))

class PersonModelTestCase(TestCase):
    """
    test Person model
    """
    fixtures = ['test_data.json']

    def test_person__str__(self):
        """
        test __str__ method returns first_name last_name
        """
        user = User.objects.get(username='admin')
        person = Person(user=user)
        self.assertEquals(person.__str__(), "Olexandr Lykhenko")

    def test_person_properties_change_user(self):
        """
        test getter and setter for name, surname, email peroperties
        test Person change affects User change
        """
        user = User.objects.get(username='admin')
        person = Person(user=user)
        self.assertEquals(person.name, "Olexandr")
        self.assertEquals(person.surname, "Lykhenko")
        self.assertEquals(person.email, "lykhenko.olexandr@gmail.com")
        person.name = "Ololoshka"
        person.surname = "Trololo"
        person.email = "ololo@lol.lol"
        self.assertEquals(person.name, "Ololoshka")
        self.assertEquals(person.surname, "Trololo")
        self.assertEquals(person.email, "ololo@lol.lol")

        self.assertEquals(user.first_name, "Ololoshka")
        self.assertEquals(user.last_name, "Trololo")
        self.assertEquals(user.email, "ololo@lol.lol")

class PersonFormTestCase(TestCase):
    """
    test PersonForm modelform from admin.py
    """
    def setUp(self):
        self.factory = RequestFactory()


    def test_form_gets_values_from_instance_user_on_init(self):
        """
        test that, given instance, form retreives name, surname, email
        values from instance.user and sets initial values of corresponding
        fields on __init__ form
        """
        user = User.objects.get(username='admin')
        person = Person(user=user)
        personform = PersonForm(instance=person)
        personfields_wishdict = {'name': 'Olexandr',
                                 'surname': 'Lykhenko',
                                 'email': 'lykhenko.olexandr@gmail.com',
                                }

        self.assertTrue(all(item in personform.initial.items() \
                        for item in personfields_wishdict.items()))


    def test_form_saves_values_to_instance_user_on_save(self):
        """
        test that, form saves name, surname, email values to corresponding User
        when commiting form
        """

        person = Person.objects.get(user__username='admin')
        personform = PersonForm(instance=person, data={'name': 'has_changed'})

        if personform.is_valid():
            person = personform.save()
            self.assertEquals(User.objects.get(pk=person.user.pk).first_name, "has_changed")
        else:
            self.fail("personform not valid")






