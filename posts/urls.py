from django.urls import path
from .views import post_view, posts_view

urlpatterns = [
    # path('', posts_view, name='posts'),
    path('', posts_view, name='posts'),
    path('<int:post_id>/', post_view, name='post'),
]
