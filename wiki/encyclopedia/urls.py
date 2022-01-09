from django.urls import path

from . import views

App_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("random", views.ashwai, name="random"),
    path("<str:name>", views.title, name="title"),
    path("<str:name>/edit", views.edit, name="edit")
]
