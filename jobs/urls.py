from . import views

from django.urls import path
from .views import JobListView


urlpatterns = [
    path("", JobListView.as_view(), name="job_list"),
    path("job/<int:pk>/", views.job_detail, name="job_detail"),
    path("job/<int:pk>/apply/", views.apply_for_job, name="apply_for_job"),
    path("post/", views.post_job, name="post_job"),
]
