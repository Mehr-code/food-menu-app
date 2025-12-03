from django.db import models
from django.urls import reverse


class Item(models.Model):

    def __str__(self):
        return self.item_name

    # This URL is for Class Base View
    def get_absolute_url(self):
        return reverse("menu:index")

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField()
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://www.foodservicerewards.com/cdn/shop/t/262/assets/fsr-placeholder.png?v=45093109498714503231652397781",
    )
