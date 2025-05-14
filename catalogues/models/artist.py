from django.db import models

from catalogues.models.type import Type  # Importation du modèle Type

class Artist(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)

    # Relation Many-to-Many via la table pivot 'artist_type'
    types = models.ManyToManyField(Type, through='ArtistType', related_name='artists')

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    class Meta:
        db_table = "artists"
