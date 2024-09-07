# jobs/filters.py
import django_filters
from .models import JobPosting


class JobPostingFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    location = django_filters.CharFilter(lookup_expr="icontains")
    expires_at = django_filters.DateFilter(lookup_expr="gte")

    class Meta:
        model = JobPosting
        fields = ["title", "location", "expires_at"]
