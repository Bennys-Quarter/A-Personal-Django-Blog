from django.db import models
from django.utils import timezone
from django.utils.text import slugify

import shutil

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    author = models.CharField(max_length=100)
    html_file = models.FileField(upload_to='blog/documents/', blank=True, null=True)
    content = models.TextField(blank=True)
    featured_image = models.ImageField(upload_to='blog/images/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)

    def prepare_html(self):
        # Path where uploaded file was stored
        media_file_path = self.html_file.path
        templates_dir = f"./blog/templates/blog/documents/"

        # Adjust default file

        begin_text = "{% extends 'blog/index.html' %}\n{% block article %}\n"
        end_text = "\n{% endblock article %}"

        remove_text = ["<!DOCTYPE html>", "<html>", "</html>","<body>", "</body>"]

        with open(media_file_path, 'r', encoding='utf-8') as f:
            file = f.read()

        for text in remove_text:
            file = file.replace(text, "")

        with open(media_file_path, 'w', encoding='utf-8') as f:
            f.write(begin_text + file + end_text)

        shutil.copy(media_file_path, templates_dir)


    def save(self, *args, **kwargs):
        if not self.slug:  # Auto-create slug from title
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

        if self.html_file:
            self.prepare_html()

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title