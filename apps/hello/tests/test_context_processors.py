from django.test import TestCase

from django.core.urlresolvers import reverse
# from django.test import Client
from django.test.client import RequestFactory


class AddDjangoSettingsContextProcessorTestCase(TestCase):
	fixtures = ['test_data.json']
	def test_djago_settings_in_context(self):
		"""
		test django_settings variable available from context
		"""
		response = self.client.get(reverse('main-page'))
		self.assertTrue('django_settings' in response.context)


