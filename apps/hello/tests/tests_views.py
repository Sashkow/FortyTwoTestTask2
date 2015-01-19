from django.test import TestCase

from django.core.urlresolvers import reverse
# from django.test import Client
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from apps.hello.models import Person

from django.contrib.auth.models import AnonymousUser

from apps.hello.utils import get_person_or_admin

class MainPageViewTestCase(TestCase):
    """
    tests for main view
    """
    fixtures = ['test_data.json']

    def setUp(self):
        pass

    def test_main_page_view_returns_200(self):
        """
        test main_page renders page successfully
        i. e. returns response with status code 200
        """
        response = self.client.get(reverse('main'))
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

        response = self.client.get(reverse('main'))
        self.assertTrue('person' in response.context)
        person = response.context['person']
        self.assertTrue(isinstance(person, Person))
        for name, value in personfields_wishdict.iteritems():
            self.assertTrue(hasattr(person, name))
            self.assertTrue(value in str(person.__getattribute__(name)))


class RequestDataViewTestCase(TestCase):
    """
    requests view test case
    """
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
        
        
class EditViewTestCase(TestCase):
    """
    edit view test case
    """
    fixtures = ['test_data.json']
    def test_returns_200(self):
        """
        test edit view returns 200 in response 
        """
        response = self.client.get(reverse('edit'))
        self.assertEquals(response.status_code, 200)

    def test_has_form_in_context(self):
        """
        test edit view returns form in response.context 
        """
        response = self.client.get(reverse('edit'))
        self.assertTrue('form' in response.context)

    def test_correct_form_data_on_get(self):
        """
        test response.context['form'] contains correct data after GET request
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

        response = self.client.get(reverse('edit'))
        form = response.context['form']
        
        for name, value in personfields_wishdict.iteritems():
            self.assertTrue(name in form.initial)
            self.assertTrue(value in str(form.initial[name]))

    def test_redirects_to_main_on_post(self):
        """
        test viwew redirects to main page after POST request
        """
        response = self.client.post(reverse('edit'))
        self.assertEquals(response.status_code, 302)
        self.assertEquals('http://testserver/',response.url) 


from django.contrib.sessions.middleware import SessionMiddleware

def add_session_to_request(request):
    """Annotate a request object with a session"""
    middleware = SessionMiddleware()
    middleware.process_request(request)
    request.session.save() 

class GetPersonOrAdminUtilTestCase(TestCase):
    """
    """
    fixtures = ['test_data.json']
    def setUp(self):
        self.factory = RequestFactory()

    def test_gets_admin_if_unauthed(self):
        request = self.factory.get(reverse('main'))
        request.user = AnonymousUser()
        add_session_to_request(request)
        self.assertEquals(get_person_or_admin(request).user.username,'admin')

    def test_gets_person_if_authed(self):
        request = self.factory.get(reverse('main'))
        request.user = User.objects.get(username='leela')
        self.assertEquals(get_person_or_admin(request).user.username,'leela')