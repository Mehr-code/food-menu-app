from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
    path("register/", views.register, name="register"),
    path(
        "login/",
        views.MyLoginView.as_view(),
        name="login",
    ),
    path("logout/", views.logout_view, name="logout"),
    path("logout-page/", views.logout_page, name="logout_page"),
    path("profile/", views.profile, name="profile"),
    path("edit/", views.ProfileUpdateView.as_view(), name="editProfile"),
]
