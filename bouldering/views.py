from django.shortcuts import render
from bouldering.models import BoulderLocation, BoulderSector, BoulderSafety, BoulderGrade, Boulder
from bouldering.serializers import BoulderSerializer, BoulderGradeSerializer, BoulderSafetySerializer, \
    BoulderSectorSerializer, BoulderLocationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework import generics
from rest_framework import mixins

class IsAuth(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated)
class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_superuser)


# BOULDERS
class AllBoulders(generics.ListCreateAPIView):
    permission_classes = [IsAuth]
    serializer_class = BoulderSerializer
    def get_queryset(self):
        return Boulder.objects.all()
    def perform_create(self, request):
        boulder = request.data
        boulder['boulder_finder']=self.request.user.id
        serializer = BoulderSerializer(data=boulder)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'Boulder added'})

class BouldersByUser(generics.ListAPIView):
    serializer_class = BoulderSerializer
    lookup_field = 'boulder_finder'
    permission_classes = [IsAuth]
    def get_queryset(self):
        return Boulder.objects.filter(boulder_finder=self.request.user.id)



class BoulderByIdUser(generics.RetrieveAPIView):
    permission_classes = [IsAuth]
    serializer_class = BoulderSerializer
    lookup_field = 'id'
    def get_queryset(self):
        return Boulder.objects.filter(id=self.kwargs['id'],boulder_finder_id=self.request.user.id)

class BoulderByIdAdmin(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAdmin]
    serializer_class = BoulderSerializer
    lookup_field = 'id'
    def get_queryset(self):
        return Boulder.objects.filter(id=self.kwargs['id'])



class BouldersByGrade(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class=BoulderSerializer
    def get_queryset(self):
        return Boulder.objects.filter(boulder_grade__boulder_grade=self.kwargs['boulder_grade'])



class BouldersByGradeLocation(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class = BoulderSerializer
    def get_queryset(self):

        return Boulder.objects.filter(boulder_grade__boulder_grade=self.kwargs['boulder_grade'],
                                          boulder_location__location_name=self.kwargs['boulder_location'])


class BouldersByGradeSectorLocation(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class = BoulderSerializer
    def get_queryset(self):
        return Boulder.objects.filter(boulder_grade__boulder_grade=self.kwargs['boulder_grade'],
                                          boulder_location__location_name=self.kwargs['boulder_location'],
                                          boulder_sector__sector_name=self.kwargs['boulder_sector'])



#EDIT
class BouldersBySafetySector(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class = BoulderSerializer
    def get_queryset(self):
        return Boulder.objects.filter(boulder_safety__safety_grade=self.kwargs['boulder_safety'],
                                      boulder_sector__sector_name=self.kwargs['boulder_sector'])




class BouldersByLocation(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class = BoulderSerializer
    def get_queryset(self):
        return Boulder.objects.filter(boulder_location__location_name=self.kwargs['boulder_location'])



class BouldersByLocationSector(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class = BoulderSerializer
    def get_queryset(self):
        return Boulder.objects.filter(boulder_location__location_name=self.kwargs['boulder_location'],
                                          boulder_sector__sector_name=self.kwargs['boulder_sector'])

###################
class BouldersByFinder(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class = BoulderSerializer
    def get_queryset(self):
        return Boulder.objects.filter(boulder_finder__username=self.kwargs['boulder_finder'])



class BouldersByName(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class = BoulderSerializer
    def get_queryset(self):
        return Boulder.objects.filter(boulder_name=self.kwargs['boulder_name'])




class BouldersBySafetyLocationSector(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class = BoulderSerializer
    def get_queryset(self):
        return Boulder.objects.filter(boulder_safety__safety_grade=self.kwargs['boulder_safety'],
                                          boulder_sector__sector_name=self.kwargs['boulder_sector'],
                                          boulder_location__location_name=self.kwargs['boulder_location'])



class BouldersBySafetyLocation(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class = BoulderSerializer
    def get_queryset(self):
        return Boulder.objects.filter(boulder_safety__safety_grade=self.kwargs['safety_grade'],
                                          boulder_location__location_name=self.kwargs['location_name'])



class BouldersBySafety(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class = BoulderSerializer

    def get_queryset(self):
        return Boulder.objects.filter(boulder_safety__safety_grade=self.kwargs['safety_grade'])



class BouldersBySaftetyGrade(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class = BoulderSerializer
    def get_queryset(self):
        return Boulder.objects.filter(boulder_safety__safety_grade=self.kwargs['safety_grade'],
                                          boulder_grade__boulder_grade=self.kwargs['boulder_grade'])



class BouldersBySafetyGradeLocation(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class = BoulderSerializer
    def get_queryset(self):
        return Boulder.objects.filter(boulder_safety__safety_grade=self.kwargs['safety_grade'],
                                          boulder_location__location_name=self.kwargs['location_name'],
                                          boulder_grade__boulder_grade=self.kwargs['boulder_grade'])

class BouldersBySafetyGradeLocationSector(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class = BoulderSerializer

    def get_queryset(self):
        return Boulder.objects.filter(boulder_safety__safety_grade=self.kwargs['safety_grade'],
                                          boulder_location__location_name=self.kwargs['location_name'],
                                          boulder_grade__boulder_grade=self.kwargs['boulder_grade'],
                                          boulder_sector__sector_name=self.kwargs['boulder_sector'])






# SECTORS

class BoulderSectorAll(generics.ListCreateAPIView):
    permission_classes = [IsAuth]
    serializer_class = BoulderSectorSerializer

    def get_queryset(self):
        return BoulderSector.objects.all()

class BoulderSectorCreate(generics.CreateAPIView):
    permission_classes = [IsAdmin]
    serializer_class = BoulderSectorSerializer




class BoulderSectorByLocation(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class = BoulderSectorSerializer
    def get_queryset(self):
        return BoulderSector.objects.filter(sector_location__location_name=self.kwargs['location_name'])

class BoulderSectorByName(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class=BoulderSectorSerializer
    def get_queryset(self):
        return BoulderSector.objects.filter(sector_name=self.kwargs['sector_name'])


class BoulderSectorById(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class = BoulderSectorSerializer
    def get_queryset(self):
        return BoulderSector.objects.filter(id=self.kwargs['id'])

class BoulderSectorByIdAdmin(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdmin]
    serializer_class = BoulderSectorSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return  BoulderSector.objects.filter(id=self.kwargs['id'])





# LOCATIONS

class BoulderLocationAll(generics.ListCreateAPIView):
    permission_classes = [IsAuth]
    serializer_class = BoulderLocationSerializer

    def get_queryset(self):
        return BoulderLocation.objects.all()



class BoulderLocationByName(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class = BoulderLocationSerializer

    def get_queryset(self):
        return BoulderLocation.objects.filter(location_name=self.kwargs['location_name'])

class BoulderLocationByIdUser(generics.ListAPIView):
    permission_classes=[IsAuth]
    serializer_class=BoulderLocationSerializer

    def get_queryset(self):
        return BoulderLocation.objects.filter(id=self.kwargs['id'])
    
class BoulderLocationByIDAdmin(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdmin]
    serializer_class = BoulderLocationSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return BoulderLocation.objects.filter(id=self.kwargs['id'])


# SAFETY

class BoulderSafetyAll(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class = BoulderSafetySerializer
    def get_queryset(self):
        return BoulderSafety.objects.all()
    
class BoulderSafetyByIdAdmin(generics.RetrieveUpdateDestroyAPIView,generics.ListCreateAPIView):
    permission_classes = [IsAdmin]
    serializer_class = BoulderSafetySerializer
    lookup_field='id'
    def get_queryset(self):
        return BoulderSafety.objects.filter(id=self.kwargs['id'])


# GRADES

class BoulderGradeAll(generics.ListCreateAPIView):
    
    serializer_class = BoulderGradeSerializer

    def get_queryset(self):
        return BoulderGrade.objects.all()
    

class BoulderGradeById(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class = BoulderGradeSerializer
    def get_queryset(self):
        return BoulderGrade.objects.filter(id=self.kwargs['id'])

class BoulderGradeByIdAdmin(generics.RetrieveUpdateDestroyAPIView,generics.ListCreateAPIView):
    permission_classes = [IsAdmin]
    serializer_class = BoulderGradeSerializer
    lookup_field='id'
    def get_queryset(self):
        return BoulderGrade.objects.filter(id=self.kwargs['id'])


