from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Book
from .serializer import Bookserializer
from .permissions import permissionsUsers
# Create your views here.
class DataView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer
    permission_classes = (permissionsUsers, IsAuthenticated)
class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer
    permission_classes = (permissionsUsers,IsAuthenticated)