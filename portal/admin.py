from django.contrib import admin
from .models import Application, Answer, Event, PortfolioFile, Question

# Register your models here.
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "status")
    list_filter = ("status",)
    prepopulated_fields = {
        "slug": ("name",),
    }
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "event",
        "required",
        "order",
    )

    list_filter = ("event", "required")


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0
    readonly_fields = ("question", "answer")

    can_delete = False


class PortfolioFileInline(admin.TabularInline):
    model = PortfolioFile
    extra = 0
    readonly_fields = ("file", "uploaded_at")

    can_delete = False


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "event",
        "submitted_at",
    )

    list_filter = ("event", "submitted_at")

    search_fields = (
        "name",
        "email",
    )

    readonly_fields = (
        "name",
        "email",
        "event",
        "submitted_at",
    )

    inlines = [
        AnswerInline,
        PortfolioFileInline,
    ]
