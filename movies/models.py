from django.db import models

class Person(models.Model):

    class Meta:
        db_table = "person"

    name = models.CharField(max_length=150)
    birthdate = models.DateField(null=True)

    def __repr__(self):
        return f"Person<id={self.id}, name={self.name}>"

    __str__ = __repr__


# Create your models here.
class Movie(models.Model):

    class Meta:
        db_table = "movie"

    class PgChoice(models.TextChoices):
        G = "G"
        PG = "PG"
        PG_13 = "PG-13"
        R = "R"
        NC_17 = "NC-17"

    class ColorChoice(models.TextChoices):
        COLOR = "COLOR"
        BLACK_AND_WHITE = "BLACK_AND_WHITE"

    # tuning attributes/fields:
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/
    # - max_length
    # - null
    # - db_column
    # - unique
    # - choices
    # - primary key

    # Primary Key: AutoField, SmallAutoField, BigAutoField
    #  - can be set by default in app config
    #  - usefull when column name is not id
    #  - no generation auto: IntegerField, ...
    # id = models.AutoField(primary_key=True) # 32 bits integer 

    title = models.CharField(max_length=300)
    year = models.IntegerField(db_column="release_year")
    duration = models.IntegerField(null=True)
    pg = models.CharField(choices=PgChoice.choices, max_length=5, null=True)
    synopsis = models.TextField(null=True)
    poster_uri = models.URLField(null=True)
    color = models.CharField(choices=ColorChoice.choices, max_length=15, null=True)
    
    # Many to One association
    # NB: 
    # - on_delete: DO_NOTHING, PROTECT, RESTRICT, 
    #       CASCADE, SET_NULL, SET_DEFAULT, SET
    # - db_column=<column name>
    # - db_index=True|False on foreign key
    director = models.ForeignKey(
        to=Person, 
        on_delete=models.DO_NOTHING, 
        null=True,
        related_name='directed_movies'
    ) 

    actors = models.ManyToManyField(
        to=Person,
        related_name='played_movies',
        null=True,
        db_table='play'
    )

    def __repr__(self):
        return f"Movie<id={self.id}, title={self.title}, year={self.year}>"

    __str__ = __repr__


