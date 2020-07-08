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



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
   

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



class FriendListView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        friends = [user.username for user in request.user.friend.all()]
        return Response(friends)

    def post(self, request, format=None):
        user_name = request.data.get('user')
        user_to_follow = User.objects.get(username=user_name)
        current_user = request.user
        current_user.friend.add(user_to_follow)
        return Response({"friend_count": current_user.friend.count()})


class FriendDetailView(views.APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, friend_username, format=None):
        user_to_remove = get_object_or_404(request.user.friend,username=friend_username)
        request.user.friend.remove(user_to_remove)
        return Response(request.data)
    
    def get(self, request, friend_username, format=None):
        user_to_view = get_object_or_404(request.user.friend,username=friend_username)
        serializer = UserSerializer(user_to_view, context={'request': request})
        return Response(serializer.data)

class CardDetailView(views.APIView):
    queryset = Card.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, request, card_id):
        card_to_show = get_object_or_404(Card, id=card_id)
        serializer = CardSerializer(card_to_show, context={'request': request})
        return Response(serializer.data)

class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)


    def get_queryset(self):
        cards = self.request.user.cards.all()
        return cards

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
    
    @action(detail=False, methods=['GET'])
    def all_cards(self, request):
        cards = Card.objects.all()
        page = self.paginate_queryset(cards)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = CardSerializer(cards, many=True, context={'request': request})
        return Response(serializer.data)