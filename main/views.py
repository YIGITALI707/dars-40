from django.shortcuts import render
from rest_framework import viewsets
from .models import Shop,Category,Firma
from .serializer import ShopSerializer,CategorySerializer,FirmaSerializer
# Create your views here.


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class =ShopSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category
    serializer_class = CategorySerializer


class FirmaViewSet(viewsets.ModelViewSet):
    queryset = Firma
    serializer_class = FirmaSerializer
