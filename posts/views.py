from django.shortcuts import get_object_or_404, render
from django.forms.models import model_to_dict
from django.views.generic.list import ListView
from django.core.paginator import Paginator

from .models import Post
from .forms import SortForm


def posts_view(request):

    template_name = "posts.html"

    if request.method == "GET":
        form = SortForm(request.GET, initial={'sort': 'any',
                                              'op': 'any',
                                              'media': 'any'})
        if form.is_valid():
            sort = form.cleaned_data.get('sort')
            op = form.cleaned_data.get('op')
            media = form.cleaned_data.get('media')

    if sort == 'notions':
        posts = Post.objects.all().order_by('-notions')
    elif sort == 'date':
        posts = Post.objects.all().order_by('-date')
    else:
        posts = Post.objects.all()

    if media == 'with':
        posts = posts.exclude(files=[])
    elif media == 'without':
        posts = posts.filter(files__exact=[])

    if op == 'with':
        posts = posts.filter(is_op=True)
    elif op == 'without':
        posts = posts.filter(is_op=False)

    return render(request, template_name, {'posts': posts, 'form': form})


def post_view(request, post_id):
    post = model_to_dict(get_object_or_404(Post, number=post_id))

    return render(request, 'post.html', post)
