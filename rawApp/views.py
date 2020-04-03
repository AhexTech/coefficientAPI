from django.shortcuts import render

# Create your views here.
from .serializers import *
from django.contrib.auth.models import *
from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.views.generic.edit import UpdateView
from django.views.generic import DetailView

from rest_framework import viewsets


from rest_framework.decorators import api_view, permission_classes
from  rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions


#
# class UserDdetailViewset(viewsets.ModelViewSet):
#     queryset = UserDetail.objects.all()
#     serializer_class = UserDetailSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def openToAll(request,*args,**kwargs):
    return Response(data='Hello User',status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted(request,*args,**kwargs):
    context={
        "Username" : request.user.username,
        "email":request.user.email,
        "first_name":request.user.first_name,
        "last_name":request.user.last_name,
        "phone":request.user.phone,

    }
    return Response(data=context,status=status.HTTP_200_OK)