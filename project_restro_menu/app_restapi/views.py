from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from app_restapi.serializers import CategorySerializer, MenuSerializer
from app_menus.models import Menu, Category

# Create your views here.
