from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.order_by('-date') #orders by most recent dates and limits to forst 5
    return render(request,'blogs/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/detail.html', {'blog':blog})
