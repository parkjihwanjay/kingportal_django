from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.Apply, name='apply'),
    path('info/', views.getInfo, name='test'),
    path('auth/', views.hashing, name='auth'),
]