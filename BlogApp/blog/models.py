from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    title = models.CharField(max_length=1000)
    description = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now =True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'blog_post'
        verbose_name_plural = 'blog_posts'
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add =    True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.comment
    
