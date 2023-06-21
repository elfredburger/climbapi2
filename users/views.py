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

        return User.objects.get(username=self.kwargs['username'])


class UserByEmail(generics.ListAPIView):
    permission_classes = [IsAdmin]
    serializer_class = UserSerializer
    def get_queryset(self):

        return User.objects.get(email=self.kwargs['email'])

class UserById(generics.RetrieveUpdateDestroyAPIView,generics.ListCreateAPIView):
    permission_classes = [IsAdmin]
    serializer_class = UserSerializer
    lookup_field = 'id'

    def get_queryset(self):

        return User.objects.filter(id=self.kwargs['id'])




class UsersByLastName(APIView):
    permission_classes = [IsAuth]

    def get(self, request, last_name):
        users = User.objects.filter(last_name=last_name)
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})


class UsersByFirstName(APIView):
    permission_classes = [IsAuth]

    def get(self, request, first_name):
        users = User.objects.filter(first_name=first_name)
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})


class UsersByFullName(APIView):
    permission_classes = [IsAuth]

    def get(self, request, first_name, last_name):
        users = User.objects.filter(first_name=first_name, last_name=last_name)
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})


# -----------------------------------------------------------------------------------------------------------------------


class AppUsers(APIView):
    permission_classes = [IsAuth]

    def get(self, request):
        users = AppUser.objects.all()
        serializer = AppUserSerializer(users, many=True)
        return Response({'users': serializer.data})
    def post(self, request):
        data = request.data
        data['user'] = self.request.user.id  # using user loged in id to change model
        serializer = AppUserSerializer(data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('user info updated')


class UsersClimedBoulder(APIView):
    permission_classes = [IsAuth]

    def get(self, request, user_id):
        boulders = AppUser.objects.filter(user__id=user_id).valueslist('user_climbed_boulders')
        serializer = AppUserSerializer(boulders, many=True)
        return Response({'climbed_boulders': serializer.data})



class UserFaBoulders(APIView):
    permission_classes = [IsAuth]

    def get(self, request, user_id):
        boulders = AppUser.objects.filter(user__id=user_id).values('user_fa_boulders')
        serializer = AppUserSerializer(boulders, many=True)
        return Response({'fa_boulders': serializer.data})


class UserFavoriteBoulders(APIView):
    permission_classes = [IsAuth]

    def get(self, request, user_id):
        boulders = AppUser.objects.filter(user__id=user_id).values('user_favorite_boulders')
        serializer = AppUserSerializer(boulders, many=True)
        return Response({'favorite_boulders': serializer.data})


class UserFoundBoulders(APIView):
    permission_classes = [IsAuth]

    def get(self, request, user_id):
        boulders = AppUser.objects.filter(user__id=user_id).values('user_found_boulders')
        serializer = AppUserSerializer(boulders, many=True)
        return Response({'found_boulders': serializer.data})
