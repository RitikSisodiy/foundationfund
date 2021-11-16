from django.shortcuts import render

# Create your views here.
def blogs(request,slug=None):
    if slug is not None:
        #for single event
        return render(request,'blogs/blog-single.html')
    # for event list
    return render(request,'blogs/blogs.html')