from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(
        max_length=200, help_text='Enter a category')

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.ManyToManyField(Category, help_text='Select a category for this post')

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id), self.slug])

    def display_category(self):
        return ', '.join(category.name for category in self.category.all()[:3])

    display_category.short_description = 'Category'

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=50)
    text = models.TextField(max_length=2000)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text