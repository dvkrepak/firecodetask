from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Store, City, Street
from .filters import StoreFilter
from .serializers import CitySerializer, StoreCreateSerializer, StoreSerializer, StreetSerializer


class CityApiView(generics.ListAPIView):
    """Get information about all cities"""
    serializer_class = CitySerializer
    queryset = City.objects.all()


class StreetApiView(generics.ListAPIView):
    """Get information about streets in a certain city"""
    serializer_class = StreetSerializer

    def get_queryset(self):
        current_city_slug = self.kwargs.get('slug')
        current_city_name = City.objects.get(slug=current_city_slug)
        return Street.objects.filter(city=current_city_name)
    

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