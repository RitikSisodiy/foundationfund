from django.shortcuts import render
from .models import Events
# Create your views here.
def events(request,slug=None):
    res = {}
    if slug is not None:
        #for single event
        res['event'] = Events.objects.get(slug=slug)
        return render(request,'events/single-event.html',res)
    # for event list
    res['events'] = Events.objects.all()
    return render(request,'events/events.html',res)