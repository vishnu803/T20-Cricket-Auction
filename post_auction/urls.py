from django.urls import path
from . import views

urlpatterns =[
    path('', views.points_table, name='points_table'),
]