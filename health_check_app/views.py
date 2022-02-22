from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import msg
from . serializers import msgSerializer

# Create your views here.
class msgs(APIView):
    def get(self, request):
        msg1 = msg.objects.all()
        serializer = msgSerializer(msg1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

