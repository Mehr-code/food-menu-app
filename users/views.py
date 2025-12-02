from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login


def register(req):
    if req.method == "POST":
        form = RegisterForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                req,
                f"خوش آمدید {username} ! حساب کاربری شما با موفقیت ایجاد شد، لطفا وارد شوید.",
            )
            return redirect("users:login")

    form = RegisterForm()
    context = {"form": form}
    return render(req, "users/register.html", context)


class MyLoginView(LoginView):
    template_name = "users/login.html"

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        messages.success(
            self.request, f"{self.request.user.username} عزیز، خوش اومدی! 😎"
        )
        return super().form_valid(form)


def logout_view(req):
    logout(req)
    return redirect("users:logout_page")


def logout_page(req):
    return render(req, "users/logout.html")
