from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'), 
    path('register/', register, name='register'),
    path('create/', create, name='create'),
    path('item/<int:item_id>/', item, name='item'),
    path('edit/<int:item_id>/', edit, name='edit'),
    path('delete/<int:item_id>/', delete, name='delete')
]