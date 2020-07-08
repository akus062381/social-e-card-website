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


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS
                or (request.user and request.user.is_authenticated))
    
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_authenticated)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly,]

    @action(detail=False, methods=['GET'])
    def info(self, request):
        user = request.user
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def my_friends(self, request):
        friends = request.user.friend.filter()
        serializer = UserSerializer(friends, many=True, context={'request': request})
        return Response(serializer.data)
    
    @action(detail=False, methods=['GET'])
    def my_followers(self, request):
        followers = request.user.fans.filter()
        serializer = UserSerializer(followers, many=True, context={'request': request})
        return Response(serializer.data)



class FriendView(views.APIView):
    permission_classes = [IsOwnerOrReadOnly,]

    def get(self, request, format=None):
        friends = [user.username for user in request.user.friend.all()]
        return Response(friends)

    def post(self, request, format=None):
        user_name = request.data.get('user')
        user_to_follow = User.objects.get(username=user_name)
        current_user = request.user
        current_user.friend.add(user_to_follow)
        return Response({"friend_count": current_user.friend.count()})


class RemoveFriendView(views.APIView):
    permission_classes = [IsOwnerOrReadOnly,]

    def post(self, request, friend_username, format=None):
        user_to_remove = get_object_or_404(request.user.friend,username=friend_username)
        request.user.friend.remove(user_to_remove)
        return Response(request.data)



class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsOwnerOrReadOnly,]

    @action(detail=False, methods=['GET'])
    def my_cards(self, request):
        cards = request.user.cards.all()
        page = self.paginate_queryset(cards)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = CardSerializer(cards, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def friends_cards(self, request):
        cards = Card.objects.filter(username__in=request.user.friend.all())
        page = self.paginate_queryset(cards)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = CardSerializer(cards, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def followers_cards(self, request):
        cards = Card.objects.filter(username__in=request.user.fans.all())
        page = self.paginate_queryset(cards)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = CardSerializer(cards, many=True, context={'request': request})
        return Response(serializer.data)