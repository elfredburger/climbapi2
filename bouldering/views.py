from django.shortcuts import render
from bouldering.models import BoulderLocation, BoulderSector, BoulderSafety, BoulderGrade, Boulder
from bouldering.serializers import BoulderSerializer, BoulderGradeSerializer, BoulderSafetySerializer, \
    BoulderSectorSerializer, BoulderLocationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import permissions

class IsAuth(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated)
class IsUber(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_superuser)


# BOULDERS
class AllBoulders(APIView):
    permission_classes = [IsAuth]

    def get(self, request):
        boulders = Boulder.objects.all()
        serializer = BoulderSerializer(boulders, many=True)
        return Response({'boulders': serializer.data})

    def post(self, request):
        boulder = request.data
        boulder['boulder_finder']=self.request.user.id
        serializer = BoulderSerializer(data=boulder)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Boulder added'})

class BouldersByUser(APIView):
    permission_classes = [IsAuth]

    def get(self,request):
        boulders=Boulder.objects.filter(boulder_finder=request.user.id)
        serializer=BoulderSerializer(boulders,many=True)
        return Response({'boulders by user'+str(request.user.username):serializer.data})

    def delete(self, request, id):
        get_object_or_404(Boulder, id=id,boulder_finder=request.user.id)
        boulder = Boulder.objects.get(id=id)
        boulder.delete()
        return Response({'Boulder removed'})
    def patch(self,request,id):
        get_object_or_404(Boulder,boulder_finder=request.user.id,id=id)
        boulder=Boulder.objects.get(boulder_finder=request.user.id,id=id)
        data=request.data
        data['boulder_finder']=self.request.user.id
        serializer=BoulderSerializer(instance=boulder,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Boulder edited')

class BoulderById(APIView):
    permission_classes = [IsAuth]

    def get(self, request, id):
        get_object_or_404(Boulder, id=id)
        boulder = Boulder.objects.get(id=id)
        serializer = BoulderSerializer(boulder)
        return Response({'boulder': serializer.data})

class BoulderByIdUber(APIView):

    permission_classes = [IsUber]

    def patch(self, request, id):
        get_object_or_404(Boulder, id=id)
        boulder = Boulder.objects.get(id=id)
        serializer = BoulderSerializer(instance=boulder, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Boulder updated'})

    def delete(self, request, id):
        get_object_or_404(Boulder, id=id)
        boulder = Boulder.objects.get(id=id)
        boulder.delete()
        return Response({'Boulder removed'})


class BouldersByGrade(APIView):
    permission_classes = [IsAuth]

    def get(self, request, boulder_grade):
        boulders = Boulder.objects.filter(boulder_grade__boulder_grade=boulder_grade)
        serializer = BoulderSerializer(boulders, many=True)
        return Response({'boulders': serializer.data})


class BouldersByGradeLocation(APIView):
    permission_classes = [IsAuth]

    def get(self, request, boulder_grade, boulder_location):
        boulders = Boulder.objects.filter(boulder_grade__boulder_grade=boulder_grade,
                                          boulder_location__location_name=boulder_location)
        serializer = BoulderSerializer(boulders, many=True)
        return Response({'boulders': serializer.data})


class BouldersByGradeSectorLocation(APIView):
    permission_classes = [IsAuth]

    def get(self, request, boulder_grade, boulder_location, boulder_sector):
        boulders = Boulder.objects.filter(boulder_grade__boulder_grade=boulder_grade,
                                          boulder_location__location_name=boulder_location,
                                          boulder_sector__sector_name=boulder_sector)
        serializer = BoulderSerializer(boulders, many=True)
        return Response({'boulders': serializer.data})


class BouldersBySafetySector(APIView):
    permission_classes = [IsAuth]

    def get(self, request, boulder_safety, boulder_sector):
        boulders = Boulder.objects.filter(boulder_safety__safety_grade=boulder_safety,
                                          boulder_sector__sector_name=boulder_sector)
        serializer = BoulderSerializer(boulders, many=True)
        return Response({'boulders': serializer.data})


class BouldersByLocation(APIView):
    permission_classes = [IsAuth]

    def get(self, request, boulder_location):
        boulders = Boulder.objects.filter(boulder_location__location_name=boulder_location)
        serializer = BoulderSerializer(boulders, many=True)
        return Response({'boulders': serializer.data})


class BouldersByLocationSector(APIView):
    permission_classes = [IsAuth]

    def get(self, request, boulder_location, boulder_sector):
        boulders = Boulder.objects.filter(boulder_location__location_name=boulder_location,
                                          boulder_sector__sector_name=boulder_sector)
        serializer = BoulderSerializer(boulders, many=True)
        return Response({'boulders': serializer.data})


class BouldersByFinder(APIView):
    permission_classes = [IsUber]

    def get(self, request, boulder_finder):
        boulders = Boulder.objects.filter(boulder_finder__finder_name=boulder_finder)
        serializer = BoulderSerializer(boulders, many=True)
        return Response({'boulders': serializer.data})


class BouldersByName(APIView):
    permission_classes = [IsAuth]

    def get(self, request, boulder_name):
        boulders = Boulder.objects.filter(boulder_name=boulder_name)
        serializer = BoulderSerializer(boulders, many=True)
        return Response({'boulders': serializer.data})


class BouldersBySafetyLocationSector(APIView):
    permission_classes = [IsAuth]

    def get(self, request, boulder_safety, boulder_location, boulder_sector):
        boulders = Boulder.objects.filter(boulder_safety__safety_grade=boulder_safety,
                                          boulder_sector__sector_name=boulder_sector,
                                          boulder_location__location_name=boulder_location)
        serializer = BoulderSerializer(boulders, many=True)
        return Response({'boulders': serializer.data})


class BouldersBySafetyLocation(APIView):
    permission_classes = [IsAuth]

    def get(self, request, safety_grade, location_name):
        boulders = Boulder.objects.filter(boulder_safety__safety_grade=safety_grade,
                                          boulder_location__location_name=location_name)
        serializer = BoulderSerializer(boulders, many=True)
        return Response({'boulders': serializer.data})


class BouldersBySafety(APIView):
    permission_classes = [IsAuth]

    def get(self, request, safety_grade):
        boulders = Boulder.objects.filter(boulder_safety__safety_grade=safety_grade)
        serializer = BoulderSerializer(boulders, many=True)
        return Response({'boulders': serializer.data})


class BouldersBySaftetyGrade(APIView):
    permission_classes = [IsAuth]

    def get(self, request, safety_grade, boulder_grade):
        boulders = Boulder.objects.filter(boulder_safety__safety_grade=safety_grade,
                                          boulder_grade__boulder_grade=boulder_grade)
        serializers = BoulderSerializer(boulders, many=True)
        return Response({'boulders': serializers.data})


class BouldersBySafetyGradeLocation(APIView):
    permission_classes = [IsAuth]

    def get(self, request, safety_grade, boulder_grade, location_name):
        boulders = Boulder.objects.filter(boulder_safety__safety_grade=safety_grade,
                                          boulder_location__location_name=location_name,
                                          boulder_grade__boulder_grade=boulder_grade)
        serializer = BoulderSerializer(boulders, many=True)
        return Response({'boulders': serializer.data})


class BouldersBySafetyGradeLocationSector(APIView):
    permission_classes = [IsAuth]

    def get(self, request, safety_grade, boulder_grade, location_name, sector_name):
        boulders = Boulder.objects.filter(boulder_safety__safety_grade=safety_grade,
                                          boulder_location__location_name=location_name,
                                          boulder_grade__boulder_grade=boulder_grade,
                                          boulder_sector__sector_name=sector_name)
        serializer = BoulderSerializer(boulders, many=True)
        return Response({'boulders': serializer.data})


# Finders


# SECTORS

class BoulderSectorAll(APIView):
    permission_classes = [IsAuth]

    def get(self, request):
        sectors = BoulderSector.objects.all()
        serializer = BoulderSectorSerializer(sectors, many=True)
        return Response({'sectors': serializer.data})

    def post(self, request):
        sector = request.data
        serializer = BoulderSectorSerializer(data=sector)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'sector added'})


class BoulderSectorByLocation(APIView):
    permission_classes = [IsAuth]

    def get(self, request, location_name):
        sectors = BoulderSector.objects.filter(sector_location__location_name=location_name)
        serializer = BoulderSectorSerializer(sectors, many=True)
        return Response({'sectors': serializer.data})


class BoulderSectorByName(APIView):
    permission_classes = [IsAuth]

    def get(self, request, sector_name):
        sectors = BoulderSector.objects.filter(sector_name=sector_name)
        serializer = BoulderSectorSerializer(sectors, many=True)
        return Response({'sectors': serializer.data})


class BoulderSectorById(APIView):
    permission_classes = [IsAuth]

    def get(self, request, id):
        get_object_or_404(BoulderSector, id=id)
        sector = BoulderSector.objects.get(id=id)
        serializer = BoulderSectorSerializer(sector)
        return Response({'sector': serializer.data})
class BoulderSectorByIdUber(APIView):
    permission_classes = [IsUber]

    def patch(self, request, id):
        get_object_or_404(BoulderSector, id=id)
        sector = BoulderSector.objects.get(id=id)
        serializer = BoulderSectorSerializer(instance=sector, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Sector updated'})

    def delete(self, request, id):
        get_object_or_404(BoulderSector, id=id)
        sector = BoulderSector.objects.get(id=id)
        sector.delete()
        return Response({'Sector removed'})


# LOCATIONS

class BoulderLocationAll(APIView):
    permission_classes = [IsAuth]

    def get(self, request):
        locations = BoulderLocation.objects.all()
        serializer = BoulderLocationSerializer(locations, many=True)
        return Response({'locations': serializer.data})


class BoulderLocationByName(APIView):
    permission_classes = [IsAuth]

    def get(self, request, location_name):
        get_object_or_404(BoulderLocation, location_name=location_name)
        location = BoulderLocation.objects.get(location_name=location_name)
        serializer = BoulderLocationSerializer(location)
        return Response({'location': serializer.data})


# SAFETY

class BoulderSafetyAll(APIView):
    permission_classes = [IsAuth]

    def get(self, request):
        safety_grades = BoulderSafety.objects.all()
        serializer = BoulderSafetySerializer(safety_grades, many=True)
        return Response({'safety_grades': serializer.data})

    def post(self, request):
        serializer = BoulderSafetySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'safety grade added'})


class BoulderSafetyByGrade(APIView):
    permission_classes = [IsAuth]

    def get(self, request, safety_grade):
        get_object_or_404(BoulderSafety, safety_grade=safety_grade)
        safety_grade = BoulderSafety.objects.get(safety_grade=safety_grade)
        serializer = BoulderSafetySerializer(safety_grade)
        return Response({'safety_grade': serializer.data})


class BoulderSafetyById(APIView):
    permission_classes = [IsAuth]

    def get(self, request, id):
        get_object_or_404(BoulderSafety, id=id)
        safety_grade = BoulderSafety.objects.get(id=id)
        serializer = BoulderSafetySerializer(safety_grade)
        return Response({'safety_grade': serializer.data})

class BoulderSafetyByIdUber(APIView):
    permission_classes = [IsUber]

    def patch(self, request, id):
        get_object_or_404(BoulderSafety, id=id)
        safety_grade = BoulderSafety.objects.get(id=id)
        serializer = BoulderSafetySerializer(instance=safety_grade, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('safety grade saved')

    def delete(self, request, id):
        get_object_or_404(BoulderSafety, id=id)
        safety_grade = BoulderSafety.objects.get(id=id)
        safety_grade.delete()
        return Response('safety grade removed')


# GRADES

class BoulderGradeAll(APIView):
    permission_classes = [IsAuth]


    def get(self, request):
        grades = BoulderGrade.objects.all()
        serializer = BoulderGradeSerializer(grades, many=True)
        return Response({'boulder_grade': serializer.data})

    def post(self, request):
        serializer = BoulderGradeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('grade added')


class BoulderGradeByGrade(APIView):
    permission_classes = [IsAuth]

    def get(self, request, boulder_grade):
        get_object_or_404(BoulderGrade, boulder_grade=boulder_grade)
        grade = BoulderGrade.objects.all(boulder_grade=boulder_grade)
        serializer = BoulderGradeSerializer(grade)
        return Response({'boulder_grade': serializer.data})


class BoulderGradeById(APIView):
    permission_classes = [IsAuth]

    def get(self, request, id):
        get_object_or_404(BoulderGrade, id)
        boulder_grade = BoulderGrade.objects.get(id=id)
        serializer = BoulderGradeSerializer(boulder_grade)
        return Response({'boulder_grade': serializer.data})

class BoulderGradeByIdUber(APIView):
    permission_classes = [IsUber]

    def patch(self, request, id):
        get_object_or_404(BoulderGrade, id)
        boulder_grade = BoulderGrade.objects.get(id=id)
        serializer = BoulderGradeSerializer(instance=boulder_grade, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('grade saved')

    def delete(self, request, id):
        get_object_or_404(BoulderGrade, id)
        boulder_grade = BoulderGrade.objects.get(id=id)
        boulder_grade.delete()
        return Response('grade removed')
