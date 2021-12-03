
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.couses , name="couses"),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
    path('<slug:slug>/', views.couses , name="singlecouse"),
    path('donate/hendlerequest/', views.hendlerequest , name="handle"),
    # path('donate/<slug:slug>/', views.paymenthandler , name="donate"),
    path('donate/<slug:slug>/', views.paypalHandler , name="donate"),
    path('getpaypalstatus/', views.getpaypalPaymentStatus , name="getpaypalstatus"),
]
