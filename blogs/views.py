from django.shortcuts import render
from .models import Blog
# Create your views here.
def blogs(request,slug=None):

    res= {}
    res['title'] = "Blogs"
    type = 'Blog'
    res['type'] = type.lower()
    res['singleurl'] = "single"+res['type']
    if slug is not None:
        #for single event
        res['blogob'] = Blog.objects.get(slug=slug)
        return render(request,'blogs/blog-single.html',res)
    res['bloglist'] = Blog.objects.filter(type=type).order_by('-time')
    # for event list
    return render(request,'blogs/blogs.html',res)
def news(request,slug = None):
    res= {}
    res['title'] = "News"
    type = 'News'
    res['type'] = type.lower()
    res['singleurl'] = "single"+res['type']
    if slug is not None:
        #for single event
        res['blogob'] = Blog.objects.get(slug=slug)
        return render(request,'blogs/blog-single.html',res)
    # for event list
    res['bloglist'] = Blog.objects.filter(type=type).order_by('-time')
    return render(request,'blogs/blogs.html',res)