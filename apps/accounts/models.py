import uuid
from pathlib import Path

from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import MEDIA_ROOT

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

def profile_avatar_path(instance, filename):
    user = instance.user
    file_id = uuid.uuid4()
    ext = Path(filename).suffix

    path = (
        MEDIA_ROOT / 
        f"avatars/user-{instance.user_id}" / 
        f"{file_id}{ext}"
    )
    return str(path)

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )
    avatar = models.ImageField(
        upload_to=profile_avatar_path,
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
