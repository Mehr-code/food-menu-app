from django.urls import path
from . import views

app_name = "menu"

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:id>", views.detail, name="detail"),
    path("update/<int:id>", views.update_item, name="update_item"),
    path("add/", views.create_item, name="create_item"),
    path("delete/<int:id>", views.delete_item, name="delete_item"),
]
