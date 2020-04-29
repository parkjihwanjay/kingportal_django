from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main, name='main'),
    path('chat/', views.Chat, name='Chat'),
    path('nick/', views.Nick, name='Chat'),
    # path('apply/', views.Apply, name='apply'),
]
