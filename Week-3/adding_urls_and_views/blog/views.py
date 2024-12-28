from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect

blogposts = {
    'post1': 'Why did putin refuse to marry?',
    'post2': 'Why did putin refuse to marry?',
    'post3': 'Why did putin refuse to marry?'
}

# Create your views here.

def starting_page(request):
    post_list = list(blogposts.keys())
    return render(request, 'blog/index.html', {
        'post_list' : post_list
    })

def posts(request):
    pass

def post_detail(request):
    pass
