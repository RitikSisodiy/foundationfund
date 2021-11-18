from django.shortcuts import render
from . models import *
# Create your views here.
def couses(request,slug=None):
    res= {}
    if slug is not None:
        #for single couse
        res['couse'] = Couses.objects.get(slug = slug)
        return render(request,'couses/single-couse.html',res)
    # for couse list
    res['couseslist'] = Couses.objects.all().order_by('-time')
    return render(request,'couses/couses.html',res)