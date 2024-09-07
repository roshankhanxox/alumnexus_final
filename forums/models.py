from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Forum(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Discussion(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    body = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        "self", null=True, blank=True, related_name="replies", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.body[:50]  # Short preview of the discussion body
