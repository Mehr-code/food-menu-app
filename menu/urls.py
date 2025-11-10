from django.urls import path
from . import views

app_name = "menu"

urlpatterns = [
    path("", views.index),
    path("detail/<int:id>", views.detail, name="detail"),
]
