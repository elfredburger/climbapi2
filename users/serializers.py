from users import models
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.AppUser

        fields='__all__'

    def create(self, validated_data):
        validated_data['user_password'] = make_password(validated_data['user_password'])
        return super(AppUserSerializer, self).create(validated_data)