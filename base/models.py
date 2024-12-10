# models.py
from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    adjusted_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

class DosaWorldMenu(models.Model):
    name = models.CharField(max_length=100)  # Menu item name
    base_price = models.DecimalField(max_digits=6, decimal_places=2)  # Price of the item

    def __str__(self):
        return self.name
