from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Post, Comment

def home(request):
    """Display the home page with all posts and comments"""
    posts = Post.objects.all().prefetch_related('comments')
    return render(request, 'home.html', {'posts': posts})

@require_POST
def create_post(request):
    """Handle post creation"""
    title = request.POST.get('title')
    description = request.POST.get('description')
    image = request.FILES.get('image')
    
    if title and description:
        post = Post.objects.create(
            title=title,
            description=description,
            image=image
        )
        return redirect('home')
    return redirect('home')

@require_POST
def add_comment(request, post_id):
    """Add a comment to a post"""
    post = get_object_or_404(Post, id=post_id)
    content = request.POST.get('content')
    
    if content:
        Comment.objects.create(
            post=post,
            content=content
        )
    return redirect('home')

@require_POST
def upvote_comment(request, comment_id):
    """Handle comment upvoting"""
    comment = get_object_or_404(Comment, id=comment_id)
    comment.upvotes += 1
    comment.save()
    return JsonResponse({
        'success': True,
        'upvotes': comment.upvotes
    })
