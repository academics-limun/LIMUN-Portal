from django.urls import path
from . import views

urlpatterns = [
    path(
        "conferences/",
        views.application_list,
        name="conference_list"
    ),
    path(
        "conferences/<slug:event_slug>/apply/",
        views.apply,
        name="conference_form"
    )
]
