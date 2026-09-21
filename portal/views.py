from django.shortcuts import get_object_or_404, redirect, render

from .forms import ApplicationForm
from .models import Answer, Application, PortfolioFile, Event

# Create your views here.
def application_list(request):
    events = Event.objects.filter(
        status=Event.Status.OPEN
    )

    return render(
        request,
        "portal/application_list.html",
        {
            "events": events,
        },
    )

def apply(request, event_slug):
    event = get_object_or_404(Event, slug=event_slug)

    questions = event.questions.all()
    if request.method == "POST":
        form = ApplicationForm(
            request.POST,
            request.FILES,
            questions=questions,
        )

        if event.status != Event.Status.OPEN:
            return redirect(
                "application_failure"
            )

        if form.is_valid():
            application = Application.objects.create(
                event=event,
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
            )

            for question in questions:
                Answer.objects.create(
                    application=application,
                    question=question,
                    answer=form.cleaned_data[f"question_{question.id}"],
                )

            for uploaded_file in form.cleaned_data["files"]:
                PortfolioFile.objects.create(
                    application=application,
                    original_filename=uploaded_file.name,
                    file=uploaded_file,
                )

            return redirect(
                "application_success",
                event_slug=event.slug,
            )
    else:
        form = ApplicationForm(questions=questions)

    return render(
        request,
        "portal/apply.html",
        {
            "event": event,
            "form": form,
        }
    )
