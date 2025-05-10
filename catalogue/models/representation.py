from django.db import models

from catalogue.models.show import Show
from catalogue.models.location import Location

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
        return f"{self.show.title} @ {self.schedule}"

    class Meta:
        db_table = "representations"
