from django.db import models

from catalogues.models.artist import Artist
from catalogues.models.type import Type

class ArtistType(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.RESTRICT, related_name='artist_types')
    type = models.ForeignKey(Type, on_delete=models.RESTRICT, related_name='artist_types')

    def __str__(self):
        return f"{self.artist.firstname} {self.artist.lastname} - {self.type.type}"

    class Meta:
        db_table = "artist_type"
