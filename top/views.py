from django.shortcuts import render
from posts.models import Post


def top_view(request):

    template_name = 'top.html'

    top_five_with_op = Post.objects.filter(is_op=True).order_by('-notions')[:5]
    top_five_without_op = Post.objects.filter(is_op=False).order_by('-notions')[:5]

    context = {'posts_w_op': top_five_with_op,
               'posts_wo_op': top_five_without_op}

    return render(request, template_name, context)
