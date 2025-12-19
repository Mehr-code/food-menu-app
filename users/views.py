from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, MyLoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from django.shortcuts import get_object_or_404


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
    else:
        form = RegisterForm()

    context = {"form": form}
    return render(req, "users/register.html", context)


class MyLoginView(LoginView):
    template_name = "users/login.html"
    form_class = MyLoginForm

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


@login_required
def profile(req):
    return render(req, "users/profile.html")


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ["image", "location"]
    template_name = "users/profile_edit.html"

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile


class ProfileDetailView(DetailView):
    model = Profile
    template_name = "users/profile.html"
    context_object_name = "profile"

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs["username"])
