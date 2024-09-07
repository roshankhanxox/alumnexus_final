from django import forms
from .models import Forum, Discussion


class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ["title", "description", "topic"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "topic": forms.Select(attrs={"class": "form-control"}),
        }


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = [
            "body",
            "parent",
        ]  # Exclude `created_by` as it will be set in the view

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # You can add additional form customization here if needed


class CommentForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ["body"]
        widgets = {
            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Add a comment",
                }
            ),
        }
