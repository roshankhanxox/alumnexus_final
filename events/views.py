from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Event, Comment
from .forms import EventForm, CommentForm
from django.contrib import messages


def event_list(request):
    events = Event.objects.all()
    return render(request, "events/event_list.html", {"events": events})


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    comments = event.comments.all()
    return render(
        request, "events/event_detail.html", {"event": event, "comments": comments}
    )


@login_required
def create_event(request):
    if request.method == "POST":
        form = EventForm(
            request.POST, request.FILES
        )  # Include request.FILES for file uploads
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect("event_list")
    else:
        form = EventForm()
    return render(request, "events/create_event.html", {"form": form})


@login_required
def add_comment(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.event = event
            comment.user = request.user
            comment.save()
            return redirect("event_detail", event_id=event.id)
    else:
        form = CommentForm()
    return render(request, "events/add_comment.html", {"form": form})


@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if event.created_by != request.user:
        messages.error(request, "You do not have permission to delete this event.")
        return redirect("event_list")

    if request.method == "POST":
        event.delete()
        messages.success(request, "Event deleted successfully!")
        return redirect("event_list")

    return render(request, "events/confirm_delete.html", {"event": event})
