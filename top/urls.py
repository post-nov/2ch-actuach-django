from django.urls import path
from .views import top_view

urlpatterns = [
    path('', top_view, name='top')
]
