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
    sector_location=serializers.PrimaryKeyRelatedField(source='sector_location.location_name', queryset=models.BoulderLocation.objects.all(),many=False)
    class Meta:
        model=models.BoulderSector
        fields='__all__'

class BoulderSerializer(serializers.ModelSerializer):
    boulder_grade=serializers.PrimaryKeyRelatedField(source='boulder_grade.boulder_grade',queryset=models.BoulderGrade.objects.all(),many=False)
    boulder_finder=serializers.PrimaryKeyRelatedField(source='boulder_finder.username',queryset=models.User.objects.all(),many=False)
    boulder_safety=serializers.PrimaryKeyRelatedField(source='boulder_safety.safety_grade',queryset=models.BoulderSafety.objects.all(),many=False)
    boulder_location = serializers.PrimaryKeyRelatedField(source='boulder_location.location_name', queryset=models.BoulderLocation.objects.all(),many=False)
    boulder_sector=serializers.PrimaryKeyRelatedField(source='boulder_sector.sector_name', queryset=models.BoulderSector.objects.all(),many=False)

    class Meta:
        model=models.Boulder
        fields='__all__'

       