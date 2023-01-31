from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('python/', views.python, name="python"),
    path('pages/<slug>/', views.page_detail, name='page_detail'),
]
