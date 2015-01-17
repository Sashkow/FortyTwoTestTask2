"""middleware"""
from models import RequestData
from django.utils import timezone
import pickle


class RequestStore(object):
    def process_request(self, request):
        if request.method == 'POST':
            request_args = request.POST
        else:
            request_args = request.GET

        if 'user' in dir(request) and request.user.username!="":
            username = request.user.username
        else:
            username = 'AnonymusUser'

        requstdata = RequestData(path=request.path, \
                                 method=request.method, \
                                 args=request_args, \
                                 username=username, \
                                 )
        requstdata.save()
        
