from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.blog, name='hello'),
    path('result', views.result, name='result'),
]