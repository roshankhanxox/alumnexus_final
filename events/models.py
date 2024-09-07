from django.db import models
from django.contrib.auth.models import User
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    image = CloudinaryField("image", blank=True, null=True)  # Cloudinary image field

    def __str__(self):
        return self.title


class Comment(models.Model):
    event = models.ForeignKey(Event, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.event.title}"
