from django.urls import path
from . import views

urlpatterns = [
    path(
        "applications/",
        views.application_list,
        name="applications_list"
    ),
    path(
        "applications/<slug:event_slug>/apply/",
        views.apply,
        name="application_form"
    )
]
