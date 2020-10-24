from django.urls import path
from .import viewsadmin

urlpatterns = [
    path('',viewsadmin.home, name= 'home'),
    path('list/', viewsadmin.produk_list, name = 'list-produk'),
    path('create/', viewsadmin.produk_create, name='create-produk'),
    path('produk/', viewsadmin.produk, name='produk')

]