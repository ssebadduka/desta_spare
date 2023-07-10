from django.db import models
# from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.

class SupplierModel(models.Model):
    name = models.CharField(max_length=100)
    contact = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name