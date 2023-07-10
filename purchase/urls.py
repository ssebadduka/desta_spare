from django.urls import path

from . import views

urlpatterns = [
    path('purchase-stock/', views.purchase_stock, name='purchase-stock'),
    path('purchase-history/', views.purchase_history, name='purchase-history'),
    path('purchase-history/<order_no>', views.delete_purchase, name='delete-purchase')
]