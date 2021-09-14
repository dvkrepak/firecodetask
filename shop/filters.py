from rest_framework import filters
from django.utils.datetime_safe import  datetime
from django.db.models import Q
from .models import City


class StoreFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        street = request.query_params.get('street')
        city = request.query_params.get('city')
        open = request.query_params.get('open')
        all_params = Q()
        
        if street: 
            current_param = Q(street_id=street)
            all_params.add(current_param, Q.AND)

        if city:
            city = City.objects.get(id=city)
            current_param = Q(city=city)
            all_params.add(current_param, Q.AND)
    
        if open:
            current_time = datetime.now().strftime("%H:%M:%S")

            if open == '1':
                current_param = Q(opening_time__lte=current_time, closing_time__gte=current_time)
                all_params.add(current_param, Q.AND)

            elif open == '0':
                current_param = Q(opening_time__gte=current_time) | Q(closing_time__lte=current_time)
                print(current_param)
                print(current_time)
                all_params.add(current_param, Q.AND)

        return queryset.filter(all_params)
