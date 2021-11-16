from django.db import models
from django.shortcuts import render
from .models import HomeSlider
# Create your views here.
def index(request):
    res = {}
    res['sliders'] = HomeSlider.objects.all()
    return render(request,'index.html',res)