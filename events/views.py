from django.shortcuts import render

# Create your views here.
def events(request,slug=None):
    if slug is not None:
        #for single event
        return render(request,'events/single-event.html')
    # for event list
    return render(request,'events/events.html')