# jobs/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import JobPosting, Application, UserProfile
from .forms import JobPostingForm, ApplicationForm
from django_filters.views import FilterView
from .filters import JobPostingFilter


class JobListView(FilterView):
    model = JobPosting
    template_name = "jobs/job_list.html"
    filterset_class = JobPostingFilter


@login_required
def job_detail(request, pk):
    job = get_object_or_404(JobPosting, pk=pk)
    return render(request, "jobs/job_detail.html", {"job": job})


@login_required
def apply_for_job(request, pk):
    job = get_object_or_404(JobPosting, pk=pk)
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.user = request.user
            application.save()

            # Send resume link to the job poster (alumni)
            send_resume_link(job.posted_by, user_profile.resume_link)

            return redirect("job_list")
    else:
        form = ApplicationForm()
    return render(request, "jobs/apply_for_job.html", {"form": form, "job": job})


def send_resume_link(alumni, resume_link):
    # Implement email sending logic here
    pass


@login_required
def post_job(request):
    if request.method == "POST":
        form = JobPostingForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            return redirect("job_list")
    else:
        form = JobPostingForm()
    return render(request, "jobs/post_job.html", {"form": form})
