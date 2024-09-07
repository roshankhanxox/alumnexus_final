# jobs/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import JobPosting, Application, UserProfile
from .forms import JobPostingForm, ApplicationForm


# jobs/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import JobPosting


from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import JobPosting


class JobListView(LoginRequiredMixin, ListView):
    model = JobPosting
    template_name = "jobs/job_list.html"
    context_object_name = "jobs"

    def get_queryset(self):
        # Start with all job postings
        queryset = JobPosting.objects.all()

        # Get the search parameters from the GET request
        title_query = self.request.GET.get("title", "")
        location_query = self.request.GET.get("location", "")

        # Apply filters if search parameters are present
        if title_query:
            queryset = queryset.filter(title__icontains=title_query)
        if location_query:
            queryset = queryset.filter(location__icontains=location_query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Check if the user is in the 'alumni' group
        context["is_alumni"] = self.request.user.groups.filter(name="alumni").exists()
        # Add search parameters back to the context so they are preserved in the form
        context["title_query"] = self.request.GET.get("title", "")
        context["location_query"] = self.request.GET.get("location", "")
        return context


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


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import JobPostingForm


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
