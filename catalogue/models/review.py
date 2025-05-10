from django.db import models
from django.contrib.auth.models import User

from catalogue.models.show import Show

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='reviews')
    show = models.ForeignKey(Show, on_delete=models.RESTRICT, related_name='reviews')
    review = models.TextField(null=True, blank=True)
    stars = models.PositiveSmallIntegerField()
    validated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.user.username} - {self.show.title} : {self.stars}"

    class Meta:
        db_table = "reviews"
        unique_together = ('show', 'user')
