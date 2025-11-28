from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(req):
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                req, f"خوش آمدید {username} ! حساب کاربری شما با موفقیت ایجاد شد."
            )
            return redirect("menu:index")

    form = UserCreationForm()
    context = {"form": form}
    return render(req, "users/register.html", context)


def signup(req):
    pass
