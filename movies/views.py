from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from movies.filters import LastnameFilterBackend, MovieFilter
from movies.models import Movie, Person
from movies.serializers import MovieSerializer, PersonSerializer


# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    filter_backends = [LastnameFilterBackend]
    lastname_origin_field = 'name'

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter
    ]

    # Backend: DjangoFilterBackend
    # https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend
    # Advanced filters (with lookup)
    # https://django-filter.readthedocs.io/en/latest/guide/usage.html#the-filter
    # Examples: 
    #   /api/movie?title=The Mule
    #   /api/movie/?year=2020
    # filterset_fields = ['title', 'year'] # used with default FilterSet (exact)
    filterset_class = MovieFilter # Custom filter set

    # Backend: filters.SearchFilter
    # https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
    # NB: lookups for customizing search for each field: 
    #   istartswith, iexact, iregex, search, icontains (default)
    # Example:
    #    /api/movie?search=gran+2016
    search_fields = ['title__istartswith', 'year__iexact']
    
    # BAckend: ordering
    # Example:
    #   /api/movie/?ordering=title
    #   /api/movie/?ordering=-year
    #   /api/movie/?ordering=duration,-title
    ordering_fields = ['title', 'year', 'duration']
    ordering = ['year', 'title'] # default ordering


    # Combine filters example:
    # /api/movie/?year=2020&ordering=duration,-title


class MovieDirectorView(APIView):

    def patch(self, request, pk, director_id):
        # print('patch movie drirector:', pk, director_id)
        try: 
            movie = Movie.objects.get(pk=pk)
            director = Person.objects.get(pk=director_id)
        except ObjectDoesNotExist:
            error_message = "Movie or director not found"
            return Response(error_message, status=status.HTTP_404_NOT_FOUND)
        movie.director = director
        movie.save()
        return Response(MovieSerializer(movie).data)


# Views: see also:
# - generic views with mixins: https://www.django-rest-framework.org/api-guide/generic-views/
# - view as function with decorator: @api_view

# Authentication + permission
# Example with group: https://gist.github.com/pythoneast/94fbd1d2b6ffdeec4c8cc774027605a0

# Media
# https://testdriven.io/blog/django-static-files/