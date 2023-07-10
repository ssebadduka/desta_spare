from django.db import models

from supplier.models import SupplierModel
from inventory.models import InventoryModel
# Create your models here.

class NewStockModel(models.Model):
    order_no = models.IntegerField(primary_key=True)
    item = models.ForeignKey(InventoryModel, on_delete=models.CASCADE)
    supplier = models.ForeignKey(SupplierModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    total_price = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item.item