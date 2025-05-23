from django.db import models

from catalogues.models.location import Location
from catalogues.models.price import Price

class ShowManager(models.Manager):
    def get_by_natural_key(self, slug, created_in):
        return self.get(slug=slug, created_in=created_in)

class Show(models.Model):
    slug = models.CharField(max_length=60, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True)
    poster_url = models.CharField(max_length=255, null=True)
    duration = models.PositiveSmallIntegerField(null=True)
    created_in = models.PositiveSmallIntegerField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='shows')
    bookable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    # Ajout de la relation ManyToMany avec Price
    prices = models.ManyToManyField(Price, related_name='shows', db_table='show_price')

    objects = ShowManager()

    def __str__(self):
        return self.title

    def natural_key(self):
        return (self.slug, self.created_in)

    class Meta:
        db_table = "shows"
        constraints = [
            models.UniqueConstraint(fields=["slug", "created_in"], name="unique_slug_created_in")
        ]
