from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("watchList", views.watchList, name="watchList"),
    path("deactivate/<int:listing_id>", views.deactivate, name="deactivate"),
    path("commento/<int:listing_id>", views.commento, name="commento"),
    path("categori/<str:category_name>", views.categori, name="categori"),
    path("<int:listing_id>", views.listing_page, name="listing_page"),
    path("editWatch/<int:listing_id>/<int:route>", views.editWatch, name="editWatch")
]
