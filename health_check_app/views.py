from rest_framework.views import APIView
from rest_framework.response import Response
from . models import msg
from . serializers import msgSerializer
import logging
import os
from rest_framework.exceptions import APIException
from django.shortcuts import render

loggers = logging.getLogger('main')

print('Hello User!')
loggers.warning('Warning message')
loggers.info('Info message')


# Create your views here.
class msgs(APIView):
    def get(self, request):
        msg1 = msg.objects.all()
        serializer = msgSerializer(msg1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
