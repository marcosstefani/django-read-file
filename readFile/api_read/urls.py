from django.urls import path, include
from .views import random_line

urlpatterns = [
    path('file/', random_line),
]
