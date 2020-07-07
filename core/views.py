from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, views
from users.models import User
from .models import Card, get_available_cards_for_user
from .serializers import UserSerializer, CardSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework import filters
from rest_framework.response import Response 
from rest_framework.decorators import action, api_view


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = [permissions.IsAuthenticated]

    @action(detail=False, methods=['GET'], permission_classes=[permissions.IsAuthenticated])
    def info(self, request):
        user = request.user
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['GET'], permission_classes=[permissions.IsAuthenticated])
    def my_friends(self, request):
        friends = request.user.friend.filter()
        serializer = UserSerializer(friends, many=True, context={'request': request})
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'], permission_classes=[permissions.IsAuthenticated])
    def my_followers(self, request):
        followers = request.user.fans.filter()
        serializer = UserSerializer(followers, many=True, context={'request': request})
        return Response(serializer.data)

class FollowFriendAdd(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        name_of_user = request.data['username']
        user_to_follow = User.objects.get(username=name_of_user)
        current_user = request.user
        current_user.friend.add(user_to_follow)
        return Response({"friend_count": current_user.friend.count()})




class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_class = [permissions.IsAuthenticated]

    @action(detail=False, methods=['GET'], permission_classes=[permissions.IsAuthenticated])
    def my_cards(self, request):
        cards = request.user.cards.all()
        page = self.paginate_queryset(cards)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = CardSerializer(cards, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['GET'], permission_classes=[permissions.IsAuthenticated])
    def friends_cards(self, request):
        cards = Card.objects.filter(username__in=request.user.friend.all())
        page = self.paginate_queryset(cards)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = CardSerializer(cards, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['GET'], permission_classes=[permissions.IsAuthenticated])
    def followers_cards(self, request):
        cards = Card.objects.filter(username__in=request.user.fans.all())
        page = self.paginate_queryset(cards)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = CardSerializer(cards, many=True, context={'request': request})
        return Response(serializer.data)