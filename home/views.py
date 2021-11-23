from django.db import models
from django.shortcuts import render
from .models import HomeSlider
from couses.models import Couses
from events.models import Events
# Create your views here.
def index(request):
    res = {}
    res['sliders'] = HomeSlider.objects.all()
    res['couseslist'] = Couses.objects.all().order_by('-time')
    res['eventlist'] = Events.objects.all().order_by('-eventTime')
    return render(request,'index.html',res)