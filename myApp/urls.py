from django.urls import path
from myApp import views

urlpatterns = [
    path('', views.index, name='index'),


]
