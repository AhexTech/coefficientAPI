from rest_framework import  serializers
from django.contrib.auth.models import *
from .models import *
from djoser.serializers import UserCreateSerializer

# class UserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#
#
# class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
#
#     class Meta:
#         model =UserDetail
#         fields = (
#             'id',
#
#             'firstName',
#             'LastName',
#             'photo',
#             'company',
#             'degisnation',
#             'url'
#         )


class UserCreateSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model =User
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone',
            'email',
            'username',
            'url'
        )