from django.test import TestCase

from django.core.urlresolvers import reverse
from django.test import Client

from datetime import datetime

from apps.hello.models import Person


# Create your tests here.
class SomeTests(TestCase):
    def test_math(self):
        assert(2+2==4)

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
        # personfields_wishlist = ['name', 'surname', 'birth_date', 'bio', 'contacts']
        personfields_wishdict = {'name':'Olexandr',
                                 'surname':'Lykhenko',
                                 'email':'lykhenko.olexandr@gmail.com',
                                 'birth_date':'1991-02-01',
                                 'bio':"Dnipropetrovsk",
                                 'contacts':'linkedin',
                                 'jabber':'sashko@42cc.co',
                                 'skype':'sashkointelcore2duo',
                                }

        response = self.client.get(reverse('main-page'))
        self.assertTrue('person' in response.context)
        person = response.context['person']
        self.assertTrue(isinstance(person, Person))
        for name, value in personfields_wishdict.iteritems():
            self.assertTrue(hasattr(person, name))
            self.assertTrue(value in str(person.__getattribute__(name)))