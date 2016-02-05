from urllib.parse import quote_plus

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone

from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    query_list = Post.objects.active()
    if request.user.is_staff or request.user.is_superuser:
        query_list = Post.objects.all()
    paginator = Paginator(query_list, 5)
    page_request_var = "page"
    page = request.GET.get("page")

    all_posts = paginator.count
    try:
        page_list = paginator.page(page)
    except PageNotAnInteger:
        page_list = paginator.page(1)
    except EmptyPage:
        page_list = paginator.page(paginator.num_pages)

    context = {
    "list": page_list,
    "page_title": "All Articles",
    "page_request_var": page_request_var,
    "all_articles": all_posts
    }
    return render(request,"post_list.html", context)

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context= {
        "form": form,
        "page_title": "Create New Post"
    }
    return render(request,"post_create.html", context)

def post_detail(request, slug):
    instance = get_object_or_404(Post, slug= slug)
    if instance.draft or instance.published_date > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    share_string = quote_plus(instance.content)
    context = {
        "title": "instance.title",
        "instance": instance,
        "share_string": share_string,
    }
    return render(request,"post_detail.html", context)

def post_edit(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug= slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Post Was Successfully Updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        #"title": "instance.title",
        #"instance": instance,
        "form": form,
        "page_title": "Edit Post"
    }
    return render(request,"post_create.html", context)


def post_delete(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id= id)
    instance.user = request.user
    instance.delete()
    messages.success(request, "Post Deleted Successfully")
    return redirect("post:list")
