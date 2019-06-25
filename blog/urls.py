from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('posts/<int:pk>-<slug:slug>/', views.post_detail, name='post_detail'),
    path('posts/new/', views.post_new, name='post_new'),
    path('posts/<int:pk>-<slug:slug>/edit/', views.post_edit, name='post_edit'),
    path('about/', views.about, name='about'),
    path('drafts/', views.drafts, name='drafts'),
    path('posts/<int:pk>-<slug>/publish/', views.post_publish, name='post_publish'),
    path('posts/<int:pk>-<slug>/remove/', views.post_remove, name='post_remove'),
    path('posts/<int:pk>-<slug:slug>/comment/', views.add_comment, name='add_comment'),
    path('comment/<int:pk>-<slug:slug>/approve/', views.approve_comment, name='approve_comment'),
    path('comment/<int:pk>-<slug:slug>/remove/', views.remove_comment, name='remove_comment'),
]