from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='tool-picker-home'),
    path('about/', views.about, name='tool-picker-about'),
]