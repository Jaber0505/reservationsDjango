from django.db import models
from django.contrib.auth.models import User

from catalogue.models.show import Show

class Review(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField()  # 1 à 5 par exemple
    comment = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} – {self.show.title} ({self.rating}/5)"

    class Meta:
        db_table = "reviews"
        unique_together = ('show', 'user')  # Un utilisateur ne peut noter qu'une fois un spectacle
