from django.db import models
from django.shortcuts import render
from .models import HomeSlider
from couses.models import Couses
from events.models import Events
from blogs.models import Blog
# Create your views here.
def index(request):
    res = {}
    res['sliders'] = HomeSlider.objects.all()
    res['couseslist'] = Couses.objects.all().order_by('-time')
    res['eventlist'] = Events.objects.all().order_by('-eventTime')
    res['bloglist'] = Blog.objects.filter(type="Blog").order_by('-time')
    res['newslist'] = Blog.objects.filter(type="News").order_by('-time')
    return render(request,'index.html',res)