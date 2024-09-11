from rest_framework import serializers
from movies.models import Movie, Person
from django.core.exceptions import ObjectDoesNotExist

# Serializers define the API representation.
# Use one of the base classes: 
#   ModelSerializer, HyperlinkedModelSerializer
#   Serializer, BaseSerializer
#   ListSerializer

# class PersonSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Person
#         # fields = ['pk', 'name', 'birthdate']
#         # fields = '__all__'
#         fields = ['url', 'pk', 'name', 'birthdate']

# class MovieSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Movie
#         # fields = ['pk', 'title', 'year', 'duration', 'director']
#         fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        # fields = ['pk', 'name', 'birthdate']
        fields = ['pk', 'name']
        # fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    # association customization: SlugRelatedField, StringRelatedField, 
    # PrimaryKeyRelatedField, HyperlinkedRelatedField, HyperlinkedIdentityField
    
    # actors = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    
    director = PersonSerializer(many=False, read_only=True)
    actors = PersonSerializer(many=True, read_only=True)

    # nested writeable
    # director = PersonSerializer(many=False, required=False)

    # # ok when create in cascade
    # def create(self, validated_data):
    #     director = None
    #     if 'director' in validated_data:
    #         director_data = validated_data.pop('director')
    #         print(director_data)
    #         # NB: see method Person.objects.get_or_create (not for this case)
    #         # if 'pk' in director_data: # TODO: pk has disappeared
    #         #     director = Person.objects.get(pk=director_data['pk'])
    #         #     # raise ObjectDoesNotExist if not exist
    #         # else:
    #         director = Person.objects.create(**director_data)
    #     movie = Movie.objects.create(director=director, **validated_data)
    #     # movie = Movie.objects.create(**validated_data)
    #     return movie

    class Meta:
        model = Movie
        # fields = ['pk', 'title', 'year', 'duration', 'director']
        fields = '__all__'
        # depth = 1 # all assoiated fields