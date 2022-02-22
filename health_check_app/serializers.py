from dataclasses import fields
from rest_framework import serializers
from . models import msg

class msgSerializer(serializers.ModelSerializer):

    class Meta:
        model = msg
        fields = '__all__'