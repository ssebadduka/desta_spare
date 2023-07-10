from django.db import models

# Create your models here.

class InventoryModel(models.Model):
    item = models.CharField(max_length=100)
    available_quantity = models.IntegerField()

    def __str__(self):
        return self.item
