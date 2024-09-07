from django import forms
from .models import Event, Comment


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description", "image"]

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter event title"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter event description"}
        )
        self.fields["image"].widget.attrs.update({"class": "form-control-file"})


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]

    widgets = {
        "comment": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
    }
