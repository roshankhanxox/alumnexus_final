from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from .forms import CustomUserCreationForm

# superuser pass asd12345      54321
# Create your views here.


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Username or password is incorrect.")
        else:
            messages.error(request, "Both fields are required.")

        """ try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "user does not exist.")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "username or password does not exist") """
    context = {}
    return render(request, "users/login_register.html")


# -------------------------------------------------------------------------------------------


def registerPage(request):
    if request.method != "POST":
        form = CustomUserCreationForm()
        role = None
    else:
        form = CustomUserCreationForm(request.POST)
        role = request.POST.get("role")
        if form.is_valid():
            user = form.save()
            # Assign the user to the appropriate group based on role
            if role == "Student":
                group = Group.objects.get(name="Student")
            elif role == "Alumni":
                group = Group.objects.get(name="Alumni")
            else:
                group = None
            if group:
                user.groups.add(group)
                user.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect("login")
        else:
            messages.error(request, "Please correct the errors below.")

    context = {"form": form, "role": role}
    return render(request, "users/register.html", context)


# ---------------------------------------------------------------------------------------


class ForgotPasswordView(FormView):
    template_name = "users/forgot_password.html"
    form_class = PasswordResetForm
    success_url = reverse_lazy("password_reset_done")

    def form_valid(self, form):
        form.save(
            request=self.request,
            email_template_name="users/password_reset_email.html",
            subject_template_name="users/password_reset_subject.txt",
        )
        messages.success(
            self.request, "Password reset link sent! Please check your email."
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "You have successfully logged out.")
        return redirect("home")
    else:
        return HttpResponseNotAllowed(["POST"])
