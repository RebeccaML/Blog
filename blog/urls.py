from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts'),
    path('posts/<int:pk>-<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/new/', views.PostCreate.as_view(), name='post_new'),
    path('posts/<int:pk>-<slug:slug>/edit/', views.PostUpdate.as_view(), name='post_edit'),
    path('about/', views.about, name='about'),
    path('drafts/', views.drafts, name='drafts'),
    path('posts/<int:pk>-<slug>/publish/', views.post_publish, name='post_publish'),
    path('posts/<int:pk>-<slug>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('posts/<int:pk>-<slug:slug>/comment/', views.add_comment, name='add_comment'),
    path('comment/<int:pk>-<slug:slug>/approve/', views.approve_comment, name='approve_comment'),
    path('comment/<int:pk>-<slug:slug>/remove/', views.remove_comment, name='remove_comment'),
]