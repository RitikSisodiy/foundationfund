
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.blogs , name="blogs"),
    path('news/', views.news , name="news"),
    path('news/<slug:slug>/', views.news , name="singlenews"),
    path('<slug:slug>/', views.blogs , name="singleblog"),
]
