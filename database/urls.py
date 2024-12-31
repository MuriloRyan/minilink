from django.urls import path

from . import views

urlpatterns = [
    path('database/register', views.database_register, name='database_register'),
]