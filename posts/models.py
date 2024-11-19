from django.db import models
from django.utils import timezone

class Post(models.Model):
    """Model for blog posts with title, description and image"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

class Comment(models.Model):
    """Model for comments with upvote functionality"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return f'Comment by {self.content[:50]}...'

    class Meta:
        ordering = ['-created_at']
