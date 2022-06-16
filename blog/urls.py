from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blogHome"),
    path("blogposts/<int:id>", views.blogposts, name="blogHome2")
]