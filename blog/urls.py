from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blog/article/<slug:slug>", views.blog_article, name='blog_article'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

