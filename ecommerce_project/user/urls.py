from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import Login, SignUp

app_name = "user"

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="store:home"), name="logout"),
    path("register/", SignUp.as_view(), name="register"),
]
