from django.test import TestCase

from django.core.urlresolvers import reverse
# from django.test import Client
from django.test.client import RequestFactory

from apps.hello.models import Person
from django.contrib.auth.models import User

from apps.hello.admin import PersonForm




class MainPageTestCase(TestCase):
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

    def test_context_contains_needed_data(self):
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

    def test_person_str_returns_first_and_last_name(self):
        """
        test __str__ method returns proper value
        """
        u = User.objects.get(username='admin')
        p = Person(user=u)
        self.assertEquals(p.__str__(), "Olexandr Lykhenko")

    def test_person_properties_name_surname_email(self):
        """
        test getter and setter for name, surname, email peroperties
        test Person change affects User change
        """
        u = User.objects.get(username='admin')
        p = Person(user=u)
        self.assertEquals(p.name, "Olexandr")
        self.assertEquals(p.surname, "Lykhenko")
        self.assertEquals(p.email, "lykhenko.olexandr@gmail.com")
        p.name = "Ololoshka"
        p.surname = "Trololo"
        p.email = "ololo@lol.lol"
        self.assertEquals(p.name, "Ololoshka")
        self.assertEquals(p.surname, "Trololo")
        self.assertEquals(p.email, "ololo@lol.lol")

        self.assertEquals(u.first_name, "Ololoshka")
        self.assertEquals(u.last_name, "Trololo")
        self.assertEquals(u.email, "ololo@lol.lol")

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
        
        self.assertTrue(all(item in personform.initial.items() 
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






