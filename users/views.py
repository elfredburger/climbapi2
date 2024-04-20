from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import AppUser
from django.contrib.auth.models import User
from users.serializers import UserSerializer, AppUserSerializer
from bouldering.views import IsAuth,IsAdmin
from rest_framework import generics


class UserAll(generics.ListCreateAPIView):
    permission_classes = [IsAdmin]
    serializer_class = UserSerializer
    def get_queryset(self):

        return User.objects.all()


class UserByUsername(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class = UserSerializer

    def get_queryset(self):

        return User.objects.filter(username=self.kwargs['username'])


class UserByEmail(generics.ListAPIView):
    permission_classes = [IsAdmin]
    serializer_class = UserSerializer
    def get_queryset(self):

        return User.objects.filter(email=self.kwargs['email'])

class UserById(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdmin]
    serializer_class = UserSerializer
    lookup_field = 'id'

    def get_queryset(self):

        return User.objects.filter(id=self.kwargs['id'])




class UsersByLastName(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class = UserSerializer
    lookup_field='last_name'
    def get_queryset(self):
        return User.objects.filter(last_name=self.kwargs['last_name'])


class UsersByFirstName(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class = UserSerializer
    lookup_field='fisrt_name'
    def get_queryset(self):
        return User.objects.filter(first_name=self.kwargs['first_name'])


class UsersByFullName(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.filter(first_name=self.kwargs['first_name'],last_name=self.kwargs['last_name'])


# -----------------------------------------------------------------------------------------------------------------------

class AppUserCreate(generics.CreateAPIView):
    serializer_class=AppUserSerializer


class AppUsers(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class = AppUserSerializer    
    def get_queryset(self):
        return AppUser.objects.all()
    
class AppUserById(generics.ListAPIView):
    permission_classes = [IsAuth]
    serializer_class=AppUserSerializer
    def get_queryset(self):
        return AppUser.objects.filter(user=self.kwargs['id'])

class UsersClimedBoulder(APIView):
    permission_classes = [IsAuth]
    def get(self, request, id):
        boulders = AppUser.objects.filter(user=id).values('user_complete_boulders')
        return Response({'complete_boulders': boulders})


class UserFaBoulders(APIView):
    permission_classes = [IsAuth]

    def get(self, request, id):
        boulders = AppUser.objects.filter(user=id).values('user_fa_boulders')
        return Response({'fa_boulders':boulders})


class UserFavoriteBoulders(APIView):
    permission_classes = [IsAuth]

    def get(self, request, id):
        boulders = AppUser.objects.filter(user=id).values('user_favorite_boulders')
        return Response({'favorite_boulders': boulders})


class UserFoundBoulders(APIView):
    permission_classes = [IsAuth]

    def get(self, request, id):
        boulders = AppUser.objects.filter(user=id).values('user_found_boulders')
        return Response({'found_boulders': boulders})
