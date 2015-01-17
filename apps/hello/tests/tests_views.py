from django.test import TestCase

from django.core.urlresolvers import reverse
# from django.test import Client
from django.test.client import RequestFactory
from apps.hello.models import Person

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


class RequestDataViewTestCase(TestCase):
    def test_view_returns_200(self):
        "test view returns code 200 in response"
        response = self.client.get(reverse('requests'))
        self.assertEquals(response.status_code, 200)

    def test_list_of_10_requests_in_context(self):
        """
        test view response context contains list of 10 request info objects 
        """
        requests_count = 10
        for i in range(requests_count):
            response = self.client.get(reverse('requests'))
        self.assertTrue('requests' in response.context)
        self.assertEquals(len(response.context['requests']), \
         requests_count)
        self.assertTrue("First Ten Requests" in response.content)


