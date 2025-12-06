from django.urls import path
from . import views

app_name = "menu"

urlpatterns = [
    path("", views.IndexClassView.as_view(), name="index"),
    # path("detail/<int:id>", views.detail, name="detail"),
    path("detail/<int:pk>", views.DetailClassView.as_view(), name="detail"),
    path("update/<int:pk>", views.UpdateClassView.as_view(), name="update_item"),
    path("add/", views.ItemCreateView.as_view(), name="create_item"),
    path("delete/<int:pk>", views.DeleteClassView.as_view(), name="delete_item"),
]
