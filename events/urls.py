from django.urls import path
from . import views

urlpatterns = [
    path("", views.event_list, name="event_list"),
    path("event/<int:event_id>/", views.event_detail, name="event_detail"),
    path("event/create/", views.create_event, name="create_event"),
    path("event/<int:event_id>/comment/", views.add_comment, name="add_comment"),
    path("event/delete/<int:event_id>/", views.delete_event, name="delete_event"),
]
