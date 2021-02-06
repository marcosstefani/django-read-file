from django.urls import path, include
from .views import file_view

urlpatterns = [
    path('file/', file_view),
]
