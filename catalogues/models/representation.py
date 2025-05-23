from django.db import models

from catalogues.models.show import Show
from catalogues.models.location import Location

class Representation(models.Model):
    show = models.ForeignKey(
        Show,
        on_delete=models.RESTRICT,
        related_name='representations',
        null=False
    )
    schedule = models.DateTimeField()
    location = models.ForeignKey(
        Location,
        on_delete=models.RESTRICT,
        related_name='representations',
        null=True
    )

    def __str__(self):
        return f"Representation {self.id}"

    class Meta:
        db_table = "representations"
