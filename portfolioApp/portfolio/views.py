from django.shortcuts import render, get_object_or_404

from decouple import config

from .models import Post
from .github_utils import fetch_repos

# Create your views here.

def home(request):
    return render(request, 'portfolio/home.html')

def list_posts(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'portfolio/list_posts.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'portfolio/post_detail.html', {'post': post})

def github_repos(request):
    username = 'Luke-Best'
    token = config('GITHUB_API_KEY')
    repos = fetch_repos(username, token)
    
    return render(request, 'portfolio/github_repos.html', {'repos': repos})