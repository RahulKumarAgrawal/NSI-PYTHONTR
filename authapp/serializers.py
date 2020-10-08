from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *
# from .enum import NormalUser
from django.contrib.auth.models import Group
class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    # def Users(self, validated_data):
    #     user = User.objects.create(**validated_data)
    #     user.set_password(validated_data['password'])
    #     user.is_staff = True
    #     user.save()

    #     return user

    # def create(self, request, id):
    #     import pdb; pdb.set_trace()
    #     user = User.objects.get(pk=id)
    #     group = Group.objects.get(name='NormalUser')
    #     if request.user.groups.filter(name='NormalUser').exists():
    #         user_type = "ADMIN"
    #     else:
    #         user_type = "NORMAL_USER"
    #     for group_data in group:
    #         # Group.objects.create(user=user, **group_data)
    #         user.groups.add(group_data)
    #     return user
