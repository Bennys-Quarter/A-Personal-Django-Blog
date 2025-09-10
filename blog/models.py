from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    author = models.CharField(max_length=100)
    html_file = models.FileField(upload_to='documents/', blank=True, null=True)
    content = models.TextField(blank=True)
    featured_image = models.ImageField(upload_to='blog/images/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:  # Auto-create slug from title
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title