from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),  # Map the feed view to the root of the feed app
    path('like/<int:post_id>/', views.like_post, name='like_post'),  # Like functionality
]