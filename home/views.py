from django.db import models
from django.shortcuts import render
from .models import HomeSlider
from couses.models import Couses
# Create your views here.
def index(request):
    res = {}
    res['sliders'] = HomeSlider.objects.all()
    res['couseslist'] = Couses.objects.all().order_by('-time')
    return render(request,'index.html',res)