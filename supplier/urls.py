from django.urls import path

from . import views

urlpatterns = [
    path('add-supplier/', views.add_supplier, name='add-supplier'),
    path('suppliers-list/', views.suppliers_list, name='suppliers-list'),
    path('suppliers-list/<name>/edit/', views.edit_supplier, name='edit-supplier'),
    path('suppliers-list/<name>', views.delete_supplier, name='delete-supplier'),
]