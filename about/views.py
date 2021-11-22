from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
from superuser.forms import GenForm
from .models import VolunteerRegister
# Create your views here.
def about(request):
    return render(request,'about/about.html')
@csrf_exempt
def volunteer(request):
    if request.method == "POST":
        resjson = {}
        form = GenForm(VolunteerRegister)
        form = form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            resjson["message"] = "Thanks For Registration We Will Get Back To You Soon :)"
            print("success")
            return JsonResponse(resjson)
        print(request.POST,request.FILES)
        pass
    return render(request,'about/volunteer.html')

def job(request):
    return render(request,'about/job-list.html')