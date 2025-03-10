from django.urls import path
from . import views

urlpatterns = [
    # redirect '' to 'home'
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('list_posts', views.list_posts, name='list_posts'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('github_repos/', views.github_repos, name='github_repos'),
]