from django.urls import path

from . import views

urlpatterns = [
    path('new-sale/', views.new_sale, name='new-sale'),
    path('sales-history/', views.sales_history, name='sales-history'),
    path('sales-history/<order_no>', views.delete_sale, name='delete-sale')
]
