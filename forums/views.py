from django.shortcuts import render, get_object_or_404, redirect
from .models import Forum, Topic, Discussion
from django.contrib.auth.decorators import login_required
from .forms import ForumForm, CommentForm  # Import ForumForm from forms.py


def forum_list(request):
    forums = Forum.objects.all()
    topics = Topic.objects.all()

    # Fetch recent replies (limit to 5 recent replies)
    recent_replies = Discussion.objects.filter(parent__isnull=False).order_by(
        "-created_at"
    )[:5]

    selected_topic = request.GET.get("topic")
    if selected_topic:
        forums = forums.filter(topic__id=selected_topic)

    context = {
        "forums": forums,
        "topics": topics,
        "recent_replies": recent_replies,  # Pass recent replies to the template
    }
    return render(request, "forums/forum_list.html", context)


def forum_list(request):
    forums = Forum.objects.all()
    topics = Topic.objects.all()  # For filters

    # Fetch the selected topic ID from the URL
    selected_topic = request.GET.get("topic")

    # Filter forums based on the selected topic ID (use topic__id for better filtering)
    if selected_topic:
        forums = forums.filter(topic__id=selected_topic)

    # Fetch the most recent replies (comments) for the sidebar
    recent_replies = Discussion.objects.order_by("-created_at")[
        :5
    ]  # Limit to the 5 most recent comments

    context = {
        "forums": forums,
        "topics": topics,
        "recent_replies": recent_replies,  # Pass recent comments to the context
    }

    return render(request, "forums/forum_list.html", context)


@login_required
def create_forum(request):
    if request.method == "POST":
        form = ForumForm(request.POST)
        if form.is_valid():
            forum = form.save(commit=False)
            forum.created_by = request.user  # Set the user who is creating the forum
            forum.save()
            return redirect(
                "forum_list"
            )  # Redirect to the forum list page or wherever appropriate
    else:
        form = ForumForm()

    return render(request, "forums/create_forum.html", {"form": form})


def forum_detail(request, pk):
    forum = get_object_or_404(Forum, pk=pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.forum = forum
            comment.created_by = request.user
            comment.save()
            return redirect("forum_detail", pk=forum.pk)
    else:
        comment_form = CommentForm()
    comments = Discussion.objects.filter(forum=forum)
    return render(
        request,
        "forums/forum_detail.html",
        {
            "forum": forum,
            "comment_form": comment_form,
            "comments": comments,
        },
    )
