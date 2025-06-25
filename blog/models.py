from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    birth_date = models.DateField()


class Article(models.Model):
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    view_count = models.PositiveIntegerField(default=0)
    
    @property
    def get_read_time(self):
        if not self.content:
            return 0
        
        words = len(self.content.split())
        return words // 200
