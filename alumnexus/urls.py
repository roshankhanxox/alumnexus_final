from django.contrib import admin
from django.urls import path, include
from alumnexus import views as views


urlpatterns = [
    path("", views.home_view, name="home"),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("events/", include("events.urls")),
    path("forums/", include("forums.urls")),
    path("jobs/", include("jobs.urls")),
]
