from django.shortcuts import render
from bouldering.models import BoulderLocation,BoulderSector,BoulderSafety,BoulderGrade,BoulderFinder,Boulder
from users.models import AppUser
from bouldering.serializers import BoulderSerializer, BoulderFinderSerializer,BoulderGradeSerializer,BoulderSafetySerializer,BoulderSectorSerializer,BoulderLocationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

#BOULDERS
class AllBoulders(APIView):
    def get(self,request):
        boulders=Boulder.objects.all()
        serializer=BoulderSerializer(boulders,many=True)
        return Response({'boulders':serializer.data})

class BoulderById(APIView):
    def get(self,request,id):
        get_object_or_404(Boulder,id=id)
        boulder=Boulder.objects.get(id=id)
        serializer=BoulderSerializer(boulder)
        return Response({'boulder':serializer.data})

class BouldersByGrade(APIView):
    def get(self,request,boulder_grade):
        boulders=Boulder.objects.filter(boulder_grade__boulder_grade=boulder_grade)
        serializer=BoulderSerializer(boulders,many=True)
        return Response({'boulders':serializer.data})

class BouldersByGradeLocation(APIView):
    def get(self,request,boulder_grade,boulder_location):
        boulders=Boulder.objects.filter(boulder_grade__boulder_grade=boulder_grade,boulder_location__location_name=boulder_location)
        serializer=BoulderSerializer(boulders,many=True)
        return Response({'boulders':serializer.data})

class BouldersByGradeSectorLocation(APIView):
    def get(self,request,boulder_grade,boulder_location,boulder_sector):
        boulders=Boulder.objects.filter(boulder_grade__boulder_grade=boulder_grade,boulder_location__location_name=boulder_location,boulder_sector__sector_name=boulder_sector)
        serializer=BoulderSerializer(boulders,many=True)
        return Response({'boulders':serializer.data})

class BouldersBySafetySector(APIView):
    def get(self,request,boulder_safety,boulder_sector):
        boulders=Boulder.objects.filter(boulder_safety__safety_grade=boulder_safety,boulder_sector__sector_name=boulder_sector)
        serializer=BoulderSerializer(boulders,many=True)
        return Response({'boulders':serializer.data})



class BouldersByLocation(APIView):
    def get(self,request,boulder_location):
        boulders=Boulder.objects.filter(boulder_location__location_name=boulder_location)
        serializer=BoulderSerializer(boulders,many=True)
        return Response({'boulders':serializer.data})

class BouldersByLocationSector(APIView):
    def get(self,request,boulder_location,boulder_sector):
        boulders=Boulder.objects.filter(boulder_location__location_name=boulder_location,boulder_sector__sector_name=boulder_sector)
        serializer=BoulderSerializer(boulders,many=True)
        return Response({'boulders':serializer.data})

class BouldersByFinder(APIView):
    def get(self,request,boulder_finder):
        boulders=Boulder.objects.filter(boulder_finder__finder_name=boulder_finder)
        serializer=BoulderSerializer(boulders,many=True)
        return Response({'boulders':serializer.data})

class BouldersByName(APIView):
    def get(self,request,boulder_name):
        boulders=Boulder.objects.filter(boulder_name=boulder_name)
        serializer=BoulderSerializer(boulders,many=True)
        return Response({'boulders':serializer.data})

class BouldersBySafetyLocationSector(APIView):
    def get(self,request,boulder_safety,boulder_location,boulder_sector):
        boulders=Boulder.objects.filtere(boulder_safety__safety_grade=boulder_safety,boulder_sector__sector_name=boulder_sector,boulder_location__location_name=boulder_location)
        serializer=BoulderSerializer(boulders,many=True)
        return Response({'boulders':serializer.data})

class BouldersBySafetyLocation(APIView):
    def get(self,request,safety_grade,location_name):
        boulders=Boulder.objects.filter(boulder_safety__safety_grade=safety_grade,boulder_location__location_name=location_name)
        serializer=BoulderSerializer(boulders,many=True)
        return Response({'boulders':serializer.data})

class BouldersBySafety(APIView):
    def get(self,request,safety_grade):
        boulders=Boulder.objects.filter(boulder_safety__safety_grade=safety_grade)
        serializer=BoulderSerializer(boulders,many=True)
        return Response({'boulders':serializer.data})

class BouldersBySaftetyGrade(APIView):
    def get(self,request,safety_grade,boulder_grade):
        boulders=Boulder.objects.filter(boulder_safety__safety_grade=safety_grade,boulder_grade__boulder_grade=boulder_grade)
        serializers=BoulderSerializer(boulders,many=True)
        return Response({'boulders':serializers.data})
class BouldersBySafetyGradeLocation(APIView):
    def get(self,request,safety_grade,boulder_grade,location_name):
        boulders=Boulder.objects.filter(boulder_safety__safety_grade=safety_grade,boulder_location__location_name=location_name,boulder_grade__boulder_grade=boulder_grade)
        serializer=BoulderSerializer(boulders,many=True)
        return Response({'boulders':serializer.data})


class BouldersBySafetyGradeLocationSector(APIView):
    def get(self,request,safety_grade, boulder_grade, location_name,sector_name):
        boulders = Boulder.objects.filter(boulder_safety__safety_grade=safety_grade, boulder_location__location_name=location_name, boulder_grade__boulder_grade=boulder_grade,boulder_sector__sector_name=sector_name)
        serializer = BoulderSerializer(boulders, many=True)
        return Response({'boulders': serializer.data})


#Finders
class AllBoulderFinders(APIView):
    def get(self,request):
        boulder_finders=BoulderFinder.objects.all()
        serializer=BoulderFinderSerializer(boulder_finders,many=True)
        return Response({'boulders finders':serializer.data})

class BoulderFinderById(APIView):
    def get(self,request,id):
        get_object_or_404(BoulderFinder,id=id)
        boulder_finder=BoulderFinder.objects.get(id=id)
        serializer=BoulderFinderSerializer(boulder_finder)
        return Response({'boulder_finder':serializer.data})

class BoulderFinderByName(APIView):
    def get(self,request,finder_name):
        get_object_or_404(BoulderFinder,finder_name=finder_name)
        boulder_finder=BoulderFinder.objects.get(finder_name=finder_name)
        serializer=BoulderSerializer(boulder_finder)
        return Response({'boulder finder':serializer.data})

#SECTORS

class BoulderSectorAll(APIView):
    def get(self,request):
        sectors=BoulderSector.objects.all()
        serializer=BoulderSectorSerializer(sectors,many=True)
        return Response({'sectors':serializer.data})

class BoulderSectorByLocation(APIView):
    def get(self,request,location_name):
        sectors=BoulderSector.objects.filter(sector_location__location_name=location_name)
        serializer=BoulderSectorSerializer(sectors,many=True)
        return Response({'sectors':serializer.data})

class BoulderSectorByName(APIView):
    def get(self,request,sector_name):
        sectors=BoulderSector.objects.filter(sector_name=sector_name)
        serializer=BoulderSectorSerializer(sectors,many=True)
        return Response({'sectors':serializer.data})

class BoulderSectorById(APIView):
    def get(self,request,sector_id):
        get_object_or_404(BoulderSector,id=sector_id)
        sector=BoulderSector.objects.get(id=sector_id)
        serializer=BoulderSectorSerializer(sector)
        return Response({'sector':serializer.data})

#LOCATIONS

class BoulderLocationAll(APIView):
    def get(self,request):
        locations=BoulderLocation.objects.all()
        serializer=BoulderLocationSerializer(locations,many=True)
        return Response({'locations':serializer.data})

class BoulderLocationByName(APIView):
    def get(self,request,location_name):
        get_object_or_404(BoulderLocation,location_name=location_name)
        location=BoulderLocation.objects.get(location_name=location_name)
        serializer=BoulderLocationSerializer(location)
        return Response({'location':serializer.data})

#SAFETY

class BoulderSafetyAll(APIView):
    def get(self,request):
        safety_grades=BoulderSafety.objects.all()
        serializer=BoulderSafetySerializer(safety_grades,many=True)
        return Response({'safety_grades':serializer.data})

class BoulderSafetyByGrade(APIView):
    def get(self,request,safety_grade):
        get_object_or_404(BoulderSafety,safety_grade=safety_grade)
        safety_grade=BoulderSafety.objects.get(safety_grade=safety_grade)
        serializer=BoulderSafetySerializer(safety_grade)
        return Response({'safety_grade':serializer.data})

#GRADES

class BoulderGradeAll(APIView):
    def get(self,request):
        grades=BoulderGrade.objects.all()
        serializer=BoulderGradeSerializer(grades,many=True)
        return Response({'grades':serializer.data})

class BoulderGradeByGrade(APIView):
    def get(self,request,boulder_grade):
        get_object_or_404(BoulderGrade,boulder_grade=boulder_grade)
        grade=BoulderGrade.objects.all(boulder_grade=boulder_grade)
        serializer=BoulderGradeSerializer(grade)
        return Response({'grade':serializer.data})