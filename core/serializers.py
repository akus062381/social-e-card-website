from django.shortcuts import render
from users.models import User
from .models import Card
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'first_name', 'last_name', 'password', 'cards', 'friend', 'is_staff']
    



class CardSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.StringRelatedField()

    class Meta:
        model = Card
        fields = [
            'id', 'url', 'title', 'username', 'message', 'background_color', 'border', 'font',
        ]