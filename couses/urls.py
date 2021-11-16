
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.couses , name="couses"),
    path('<slug:slug>/', views.couses , name="singlecouse"),
]
