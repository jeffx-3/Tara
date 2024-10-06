from django.shortcuts import render
from .models import Post

# blog list(home) view
def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'blog_list.html',  {'posts': posts})
#blog view
def blog_detail(request):
    return render(request, 'blog_detail.html')

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