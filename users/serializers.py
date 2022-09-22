from users import models
from rest_framework import serializers

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        models=models.AppUser
        fields='__all__'