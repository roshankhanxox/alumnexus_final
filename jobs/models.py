# jobs/models.py
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class JobPosting(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    posted_by = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # Ensure this is an alumni

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.job.title}"
