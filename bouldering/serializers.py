from rest_framework import serializers
from bouldering import models
from django.core import validators

class BoulderLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.BoulderLocation
        fields='__all__'
        extra_kwargs={'location_name':{'required':True,
                                       'validators':[validators.MaxLengthValidator(50),
                                                     validators.MinLengthValidator(2)]},
                      'location_info':{'required':True,
                                       'validators':[validators.MaxLengthValidator(400),
                                                     validators.MinLengthValidator(10)]}}



class BoulderGradeSerializer(serializers.ModelSerializer):
    class Meta:
        grade=serializers.RelatedField(source='boulder_grade',read_only=True)
        model=models.BoulderGrade
        fields='__all__'

class BoulderSafetySerializer(serializers.ModelSerializer):
     class Meta:
        model=models.BoulderSafety
        fields='__all__'

class BoulderSectorSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.BoulderSector
        fields='__all__'

class BoulderSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Boulder
        fields='__all__'

