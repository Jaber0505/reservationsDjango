from django.db import models

from catalogues.models.show import Show
from catalogues.models.price import Price

class PriceShow(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    price = models.ForeignKey(Price, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.show.title} - {self.price.type} : {self.price.price}"

    class Meta:
        db_table = "price_show"
