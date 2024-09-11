from typing import override
from rest_framework import filters
import django_filters

from movies.models import Movie

class LastnameFilterBackend(filters.BaseFilterBackend):

    @override # python 3.12
    def filter_queryset(self, request, queryset, view):
        # queryset: previous queryset in filter chain
        # request: accessing request context, params
        # view: accessing attributes for this filter
        lastname = request.query_params.get('lastname', None)
        if lastname is None or not hasattr(view, 'lastname_origin_field'):
            return queryset
        field_name = view.lastname_origin_field
        filter_param = { f"{field_name}__iendswith": lastname }
        return queryset.filter(**filter_param)
    

class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = {
            'year': ['exact', 'gt', 'gte' ,'lt' , 'lte'],
            'duration': ['exact', 'gt', 'gte' ,'lt' , 'lte'],
            #'title': ['iexact', 'icontains'],
        }