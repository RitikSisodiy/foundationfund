from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'about/about.html')

def volunteer(request):
    return render(request,'about/volunteer.html')

def job(request):
    return render(request,'about/job-list.html')