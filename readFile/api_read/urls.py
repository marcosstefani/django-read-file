from django.urls import path, include
from .views import random_line, highest_occurrence

urlpatterns = [
    path('file/', random_line),
    path('char/', highest_occurrence),
]
