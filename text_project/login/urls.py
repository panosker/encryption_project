from django.urls import path
from .views import (
    UserRegistration,
    LoginView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
    LogoutView,
)

urlpatterns = [
    path("", LoginView.as_view(), name="login"),
    path("register/", UserRegistration, name="register"),
    path("change-password/", PasswordChangeView.as_view(), name="password_change"),
    path("reset-password/", PasswordResetView.as_view(), name="password_reset"),
    path(
        "set-new-password/",
        PasswordResetConfirmView.as_view(),
        name="confirm_reset_password",
    ),
    path("logout/", LogoutView, name="logout"),
]
