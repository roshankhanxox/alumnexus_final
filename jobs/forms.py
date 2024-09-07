from django import forms
from .models import (
    JobPosting,
    Application,
    UserProfile,
)  # Make sure JobPosting is used instead of Job


class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = [
            "title",
            "company",
            "location",
            "description",
            "requirements",
            "salary",
            "expires_at",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "company": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "requirements": forms.Textarea(attrs={"class": "form-control"}),
            "salary": forms.NumberInput(attrs={"class": "form-control"}),
            "expires_at": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["cover_letter"]
