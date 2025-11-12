from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def register(req):
    form = UserCreationForm()
    context = {"form": form}
    return render(req, "users/register.html", context)


def signup(req):
    pass
