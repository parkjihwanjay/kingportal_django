from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login, name='login'),
    path('apply/', views.Apply, name='apply'),
    path('info/', views.getInfo, name='test',)
]