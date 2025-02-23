from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Like

@login_required
def feed(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'feed/feed.html', {'posts': posts})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    Like.objects.get_or_create(post=post, user=request.user)
    return redirect('feed')