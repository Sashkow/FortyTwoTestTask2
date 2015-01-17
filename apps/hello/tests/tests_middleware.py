from django.test import TestCase

from django.core.urlresolvers import reverse
# from django.test import Client
from django.test.client import RequestFactory

from apps.hello.models import RequestData
from apps.hello.middleware import RequestStore

import pickle

class RequestStoreMiddlewareTest(TestCase): 
    def setUp(self):
        self.factory = RequestFactory()

    def test_middleware_updates_database(self):
        """
        test whether :model:`RequestData` amount is increased when request is made
        (functional test)
        """
        requestdata_count = len(RequestData.objects.all())

        self.client.get('fake/url')

        self.assertTrue(len(RequestData.objects.all()) > requestdata_count)

    def test_middleware_updates_database_correctly(self):
        """
        test data in :model:`RequestData` matches actual request 
        """

        request = self.factory.get('fake/url')
        requeststore = RequestStore()
        requeststore.process_request(request)
        pickled_request = pickle.dumps(request.REQUEST)

        requestdata = RequestData.objects.latest('pub_date')
        pickled_request_db = requestdata.pickled_request

        self.assertEquals(pickled_request_db, pickled_request)