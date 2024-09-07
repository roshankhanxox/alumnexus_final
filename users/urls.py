from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("register/", views.registerPage, name="register"),
    path(
        "forgot-password/", views.ForgotPasswordView.as_view(), name="forgot_password"
    ),
    # Password reset URLs
    path(
        "password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("logout/", views.logout_view, name="logout"),  # Use your custom logout view
]
