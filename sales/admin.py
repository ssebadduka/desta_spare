from django.contrib import admin

from .models import SalesModel, CustomerModel
# Register your models here.

admin.site.register(SalesModel)
admin.site.register(CustomerModel)