from django.shortcuts import render
from .models import Post

# Create your views here.
def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'blog_list.html',  {'posts': posts})

def blog_detail(request):
    return render(request, 'blog_detail.html')