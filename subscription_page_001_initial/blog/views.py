from django.shortcuts import render,HttpResponse
from .models import Post
# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(
        request,
        template_name='blog/blog.html',
        context={
            'posts':posts
        }
    )
