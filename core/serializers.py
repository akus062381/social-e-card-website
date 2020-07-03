from django.shortcuts import render
from users.models import User
from .models import Card
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'password', 'friend']
    



class CardSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Card
        fields = [
            'message', 'background_color', 'border', 'font',
        ]