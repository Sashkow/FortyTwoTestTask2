from django.test import TestCase

from django.core.urlresolvers import reverse
from django.test import Client


# Create your tests here.
class SomeTests(TestCase):
    def test_math(self):
        assert(2+2==4)

class MainPageTestCase(TestCase):
	def setUp(self):
		pass

	def test_main_page_view_returns_200(self):
		response = self.client.get(reverse('main-page'))
		self.assertEquals(response.status_code, 200)

	def test_context_contains_needed_data(self):
		response = self.client.get(reverse('main-page'))
		self.assertTrue('person' in response.context)


