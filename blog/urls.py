from django.conf.urls import include, url
from django.contrib import admin

from .views import (
post_list,
post_detail,
post_create,
post_edit,
post_delete,
recent_posts,
)

urlpatterns = [
    url(r'^$', recent_posts, name='recent_posts'),
    url(r'^post/$', post_list, name="list"),
    url(r'^post/create/$', post_create, name="create"),
    url(r'^post/(?P<slug>[\w-]+)/$', post_detail, name="detail"),
    url(r'^post/(?P<slug>[\w-]+)/edit/$', post_edit, name="edit"),
    url(r'^post/delete/$', post_delete, name="delete"),

    ]
