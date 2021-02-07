from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name="memess-api"),
    path('<int:pk>/', views.PostParticular.as_view(), name="memess-api-p"),
]
