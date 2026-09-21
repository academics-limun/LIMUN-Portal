from django import forms

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    widget = MultipleFileInput

    def clean(self, data, initial=None):
        if not data:
            return []

        if not isinstance(data, (list, tuple)):
            data = [data]

        return [
            super().clean(file, initial)
            for file in data
        ]

class ApplicationForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        label="Name",
    )

    email = forms.EmailField(
        label="Email",
    )

    files = MultipleFileField(
        required=False,
        label="Previous work",
    )

    def __init__(self, *args, questions=None, **kwargs):
        super().__init__(*args, **kwargs)

        questions = questions or []

        for question in questions:
            self.fields[f"question_{question.id}"] = forms.CharField(
                label=question.text,
                required=question.required,
                widget=forms.Textarea,
            )

    def clean_files(self):
        files = self.cleaned_data["files"]

        if len(files) > 5:
            raise forms.ValidationError(
                "You can upload a maximum of 5 files."
            )

        return files
