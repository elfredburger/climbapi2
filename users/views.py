from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import AppUser
from django.contrib.auth.models import User
from users.serializers import UserSerializer, AppUserSerializer
from bouldering.views import IsAuth,IsUber


class UserAll(APIView):
    permission_classes = [IsUber]
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'users': serializer.data})

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('User added')


class UserByUsername(APIView):
    permission_classes = [IsAuth]

    def get(self, request, username):
        get_object_or_404(User, username=username)
        user = User.objects.get(username=username)
        serializer = UserSerializer(user)
        return Response({'user': serializer.data})


class UserByEmail(APIView):
    permission_classes = [IsUber]

    def get(self, request, email):
        get_object_or_404(User, email=email)
        users = User.objects.get(email=email)
        serializer = UserSerializer(users)
        return Response({'users': serializer.data})


class UserById(APIView):
    permission_classes = [IsUber]

    def get(self, request, id):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response({'users': serializer.data})

    def patch(self, request, id):
        get_object_or_404(User, id=id)
        user = User.objects.get(id=id)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('User saved')

    def delete(self, request, id):
        get_object_or_404(User, id)
        user = User.objects.get(id=id)
        user.delete()
        return Response('User removed')


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
