from rest_framework import serializers
from .models import Store, City, Street


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class StreetSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Street
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)
    street = serializers.SlugRelatedField(slug_field='name', read_only=True)

    
    class Meta:
        model = Store
        fields = '__all__'

class StoreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
