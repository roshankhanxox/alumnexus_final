from django.urls import path
from . import views

urlpatterns = [
    path("", views.forum_list, name="forum_list"),
    path("<int:pk>/", views.forum_detail, name="forum_detail"),
    path("create/", views.create_forum, name="create_forum"),
]
