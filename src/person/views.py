from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework import authentication, permissions
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)

from .models import Author, Book
from .serializers import BookSerializer, AuthorSerializer
# Create your views here.

class AuthorList(ListModelMixin, GenericAPIView, CreateModelMixin):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return self.create(request, *args, **kwargs)
        return serializer.errors

class AuthorRetrieve(GenericAPIView, RetrieveModelMixin, UpdateModelMixin):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class AuthList(APIView):
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, format=None):
        teste = request.META.get('HTTP_AUTHORIZATION')
        return Response({"Auth: ": teste})

class BookList(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()