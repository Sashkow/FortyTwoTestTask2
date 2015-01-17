"""middleware"""
from models import RequestData
from django.utils import timezone
import pickle


class RequestStore(object):
    def process_request(self, request):
        pickled_request = pickle.dumps(request.REQUEST)
        requstdata = RequestData(pickled_request=pickled_request)
        requstdata.save()
        