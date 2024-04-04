from django.urls import path
from . import views

urlpatterns = [
    path('', views.mySite, name = 'mySite'),
    path('about/', views.About, name = 'About'),
    path('fetch/' ,views.fetchAPI, name= 'fetchAPI')
]