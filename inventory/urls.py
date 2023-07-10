from django.urls import path

from . import views

urlpatterns = [
    path('', views.sign_in, name='sign-in'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('index/', views.index, name='index'),
    path('logout/', views.log_out, name='logout'),
    path('add-stock/', views.add_stock, name='add-stock'),
    path('add-stock/<item>/edit/', views.edit_stock, name='edit-stock'),
    path('add-stock/<item>', views.delete_stock, name='delete-stock')
]