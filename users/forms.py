from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        error_messages={
            "required": "لطفا ایمیل خود را وارد کنید.",
            "invalid": "ایمیل وارد شده معتبر نیست.",
        },
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].error_messages = {
            "required": "لطفا نام کاربری را وارد کنید.",
            "unique": "این نام کاربری قبلا ثبت شده است!",
        }

        self.fields["password1"].error_messages = {
            "required": "رمز عبور را وارد کنید.",
            "password_too_short": "رمز عبور خیلی کوتاه است!",
        }

        self.fields["password2"].error_messages = {
            "required": "تکرار رمز عبور را وارد کنید.",
            "password_mismatch": "رمزهای عبور با هم مطابقت ندارند!",
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            self.add_error(None, "رمزهای عبور یکسان نیستند 😐")
        return cleaned_data


class MyLoginForm(AuthenticationForm):
    error_messages = {
        "invalid_login": "نام کاربری یا رمز عبور اشتباهه 😕 دوباره تلاش کن.",
        "inactive": "حساب کاربری شما فعال نیست.",
    }
