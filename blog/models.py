from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    options = (
        ('draft','Draft'),
        ('published','Published'),
    )
    
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    published_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    content = models.TextField()
    status = models.CharField(max_length=20, choices=options, default='draft')

    class Meta:
        ordering = ['published_date','status']
    
    def __str__(self):
        return self.title