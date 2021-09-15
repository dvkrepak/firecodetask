from rest_framework import generics, viewsets, status
from django.core.exceptions import BadRequest, ObjectDoesNotExist
from rest_framework.response import Response

from .models import Store, City, Street
from .filters import StoreFilter
from .serializers import CitySerializer, StoreCreateSerializer, StoreSerializer, StreetSerializer


class CityApiView(generics.ListAPIView):
    """Get information about all cities localhost/city/"""
    serializer_class = CitySerializer
    try: 
        queryset = City.objects.all()
    except ObjectDoesNotExist:
        raise BadRequest("Invalid Request. No cities found in the DB")


class StreetApiView(generics.ListAPIView):
    """Get information about streets in a certain city localhost/<city_slug>/street/"""
    serializer_class = StreetSerializer

    def get_queryset(self):
        try:
            current_city_slug = self.kwargs.get('slug')
            current_city_name = City.objects.get(slug=current_city_slug)
            return Street.objects.filter(city=current_city_name)
        except ObjectDoesNotExist:
            raise BadRequest(f"Invalid Request. I can't find this city in the DB or there are no cities in it")


class StoreApiView(viewsets.ModelViewSet):
    """GET/POST request handler for localhost/shop/"""
    queryset = Store.objects.all()
    filter_backends = (StoreFilter, )

    def get_serializer_class(self):
        if self.action == 'list':
            return StoreSerializer
        return StoreCreateSerializer

    # Copied from ModelViewSet-viewsets-mixins-CreateModelMixin. I added created_object 
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        created_object = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(created_object.id, status=status.HTTP_201_CREATED, headers=headers)