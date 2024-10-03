from rest_framework import serializers
from .models import Category,Shop,Firma


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shop
        fields='__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'



class FirmaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Firma
        fields='__all__'
