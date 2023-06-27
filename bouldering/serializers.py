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
class BoulderPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.BoulderPhoto
        fields='__all__'
class BoulderSerializer(serializers.ModelSerializer):
    
    boulder_grade=serializers.PrimaryKeyRelatedField(source='boulder_grade.boulder_grade',queryset=models.BoulderGrade.objects.all(),many=False)
    boulder_finder=serializers.PrimaryKeyRelatedField(source='boulder_finder.username',queryset=models.User.objects.all(),many=False)
    boulder_safety=serializers.PrimaryKeyRelatedField(source='boulder_safety.safety_grade',queryset=models.BoulderSafety.objects.all(),many=False)
    boulder_location = serializers.PrimaryKeyRelatedField(source='boulder_location.location_name', queryset=models.BoulderLocation.objects.all(),many=False)
    boulder_sector=serializers.PrimaryKeyRelatedField(source='boulder_sector.sector_name', queryset=models.BoulderSector.objects.all(),many=False) 
#untested
    def create(self, validated_data):
        # assuming you're sending images in a list
        photos = validated_data.pop('boulder_photos') # this is your key name that you'll send in request
        boulder = models.Boulder.objects.create(**validated_data)
        boulder.boulder_photos.add(*photos) # pass images list at once
        return boulder

    class Meta:
        model=models.Boulder
        fields=('boulder_name','boulder_finder','boulder_grade','boulder_safety','boulder_sector','boulder_coords','boulder_info','boulder_photos','boulder_location')


