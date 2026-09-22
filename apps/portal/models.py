from pathlib import Path
from uuid import uuid4

from django.conf import settings
from django.db import models

# Create your models here.
class Event(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        OPEN = "open", "Open"
        CLOSED = "closed", "Closed"

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    def __str__(self):
        return self.name


class Question(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="questions",
    )
    text = models.TextField()
    required = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.text


class Application(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="applications"
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="applications",
    )
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.event}"


class Answer(models.Model):
    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        related_name="answers",
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )
    answer = models.TextField()

    def __str__(self):
        return f"{self.application} - {self.question}"

def portfolio_upload_path(instance, filename):
    application = instance.application

    uid = uuid4()
    ext = Path(filename).suffix

    return (
        "media/applications/"
        f"{application.event.slug}"
        f"user-{application.user_id}"
        f"{uid}{ext}"
    )


class PortfolioFile(models.Model):
    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        related_name="portfolio_files",
    )
    original_filename = models.CharField(
        max_length=255
    )
    file = models.FileField(
        upload_to=portfolio_upload_path
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
