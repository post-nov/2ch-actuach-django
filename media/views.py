from django.shortcuts import render
from .models import Media


def media_view(request):
    template_name = 'media.html'
    media = Media.objects.exclude(files=[]).exclude(is_op=True).order_by('-notions')
    return render(request, template_name, {'media': media})
