from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="profilepic.png", upload_to="profile_pictures")
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("users:profile")
