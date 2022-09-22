from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from users.models import AppUser
from users.serializers import AppUserSerializer

# Create your views here.
class UserAll(APIView):
    def get(self,request):
        users=AppUser.objects.all()
        serializer=AppUserSerializer(users,many=True)
        return Response({'users':serializer.data})
class UsersClimedBoulder(APIView):
    def get(self,request,username):
        boulders=AppUser.objects.filter(username=username).valueslist('user_climbed_boulders')
        serializer=AppUserSerializer(boulders,many=True)
        return Response({'climbed_boulders':serializer.data})

class UserFaBoulders(APIView):
    def get(self,request,username):
        boulders=AppUser.objects.filter(username=username).values('user_fa_boulders')
        serializer=AppUserSerializer(boulders,many=True)
        return Response({'fa_boulders':serializer.data})

class UserFavoriteBoulders(APIView):
    def get(self,request,username):
        boulders=AppUser.objects.filter(username=username).values('user_favorite_boulders')
        serializer=AppUserSerializer(boulders,many=True)
        return Response({'favorite_boulders':serializer.data})

class UserFoundBoulders(APIView):
    def get(self,request,username):
        boulders=AppUser.objects.filter(username=username).values('user_found_boulders')
        serializer=AppUserSerializer(boulders,many=True)
        return Response({'found_boulders':serializer.data})

class UsersBySecondName(APIView):
    def get(self,request,user_second_name):
        users=AppUser.objects.filter(user_second_name=user_second_name)
        serializer=AppUserSerializer(users,many=True)
        return Response({'users':serializer.data})

class UsersByFirstName(APIView):
    def get(self,request,user_first_name):
        users=AppUser.objects.filter(user_first_name=user_first_name)
        serializer=AppUserSerializer(users,many=True)
        return Response({'users':serializer.data})



class UserByUsername(APIView):
    def get(self,request,username):
        get_object_or_404(AppUser,username=username)
        user=AppUser.objects.get(username=username)
        serializer=AppUserSerializer(user)
        return Response({'user':serializer.data})

class UserByEmail(APIView):
    def get(self,request,user_email):
        get_object_or_404(AppUser,user_email=user_email)
        users=AppUser.objects.get(user_email=user_email)
        serializer=AppUserSerializer(users)
        return Response({'users':serializer.data})

class UserByFullName(APIView):
    def get(self,request,user_first_name,user_second_name):
        users=AppUser.objects.filter(user_first_name=user_first_name,user_second_name=user_second_name)
        serializer=AppUserSerializer(users,many=True)
        return Response({'users':serializer.data})