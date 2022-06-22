from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model) :
    """A post made by the user."""
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(default=timezone.now)

    class Meta:
        """Sort results so recently published posts appear first"""
        ordering = ('-published_date',)

    def __str__(self):
        """Returns a string representation of the model."""
        return self.title