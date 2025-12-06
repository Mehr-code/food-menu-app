from django.contrib.auth import get_user_model
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

User = get_user_model()

username = "admin"
email = "admin@python.com"
password = "t4st!38!"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Superuser created!")
else:
    print("Superuser already exists.")
