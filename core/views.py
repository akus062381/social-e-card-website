from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, views
from users.models import User
from .models import Card, get_available_cards_for_user
from .serializers import UserSerializer, CardSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework import filters
from rest_framework.response import Response 
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = [permissions.IsAuthenticated]

    @action(detail=False, methods=['GET'], permission_classes=[permissions.IsAuthenticated])
    def my_friends(self, request):
        friends = request.user.friend.all()
        serializer = UserSerializer(friends, many=True, context={'request': request})
        return Response(serializer.data)

class UserCardView(views.APIView):
    def get(self, request, username, format=None):
        user = get_object_or_404(User, username=username)
        serializer = CardSerializer(user.cards.filter(), many=True, context={'request': request})

        return Response(serializer.data)

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    @action(detail=False, methods=['GET'], permission_classes=[permissions.IsAuthenticated])
    def my_cards(self, request):
        cards = request.user.cards.all()
        serializer = CardSerializer(cards, many=True, context={'request': request})
        return Response(serializer.data)


   # permission_classes = [
    #     IsOwnerOrReadOnly,
    # ]

    # def get_queryset(self):
    #     queryset = get_available_cards_for_user(Card.objects.all(), self.request.user)

    #     return queryset
    
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
   
