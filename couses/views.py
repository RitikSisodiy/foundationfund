from django.shortcuts import render

# Create your views here.
def couses(request,slug=None):
    if slug is not None:
        #for single couse
        return render(request,'couses/single-couse.html')
    # for couse list
    return render(request,'couses/couses.html')