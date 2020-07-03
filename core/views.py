from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, views
from users.models import User
from .models import Card
from .serializers import UserSerializer, CardSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework import filters

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
        

class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
   
