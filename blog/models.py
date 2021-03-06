from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

def user_directory_path(instance,filename):
    return 'blog/{0}/{1}'.format(instance.id,filename)


class Category (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft','Draft'),
        ('published','Published'),
    )
    
    title = models.CharField(max_length=50)
    category = models.ManyToManyField(Category)
    slug = models.CharField(max_length=50)
    published_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    image = models.ImageField(upload_to=user_directory_path, default='blog/default.jpg')
    content = models.TextField()
    status = models.CharField(max_length=20, choices=options, default='draft')

    objects = models.Manager() #default manager
    newmanager = NewManager() #custom manager

    def get_absolute_url(self):
        return reverse('blog:detailpost',args=[self.slug])

    class Meta:
        ordering = ['-published_date']
    
    def __str__(self):
        return self.title


class Comment(MPTTModel):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    parent = TreeForeignKey('self',on_delete=models.CASCADE, null=True,blank=True, related_name='children')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ["-publish"]

    def __str__(self):
        return f"Comment {self.content} - by.{self.name}"
