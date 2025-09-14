from django.shortcuts import render

from .models import BlogPost

def index(request):
    blog_posts = BlogPost.objects.order_by("created_at")
    content = {"blog_posts": blog_posts}
    return render(request, "blog/content-card.html", content)

def blog_article(request, slug):
    blog = BlogPost.objects.get(slug=slug)
    content = {"blog_content": blog}
    return render(request, f"blog/documents/post.html", content)