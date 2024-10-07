from django.shortcuts import render,get_object_or_404,redirect
from .models import Post

# blog list(home) view
def blog_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog_list.html', context)
#
# Post Detail View
def blog_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog_detail.html', {'post': post})


#search view
def search(request):
    query = request.GET.get('q', '') # Get the search term from the query parameters
    if query:
        results = Post.objects.filter(title__icontains=query)
    else:
        results = Post.objects.none() # No search results if no query
        
    context = {
        'results': results,
        'query': query,
    }
    return render(request, 'Post_search.html', context)