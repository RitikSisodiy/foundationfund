from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def about(request):
    return render(request,'about/about.html')
@csrf_exempt
def volunteer(request):
    if request.method == "POST":
        pass
    return render(request,'about/volunteer.html')

def job(request):
    return render(request,'about/job-list.html')