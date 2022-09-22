from rest_framework import serializers
from bouldering import models

class BoulderLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.BoulderLocation
        fields='__all__'

class BoulderFinderSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.BoulderFinder
        fields='__all__'

class BoulderGradeSerializer(serializers.ModelSerializer):
    class Meta:
        grade=serializers.RelatedField(source='boulder_grade',read_only=True)
        model=models.BoulderGrade
        fields=('boulder_grade','grade')

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

