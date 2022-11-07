from users import models
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'


        #THIS CUSTOM USER SERIALIZER TO BE IMPLEMENTED
class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.AppUser

        fields='__all__'

