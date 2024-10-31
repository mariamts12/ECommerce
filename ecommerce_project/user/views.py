from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_http_methods

from .forms import RegisterForm


# Create your views here.
class Login(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
    extra_context = {"title": "Login"}


class SignUp(View):
    @method_decorator(require_http_methods(["POST"]))
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            next_page = request.POST.get("next") or "/"
            return redirect(next_page)
        else:
            return render(request, "register.html", {"form": form})

    @method_decorator(require_http_methods(["GET"]))
    def get(self, request):
        form = RegisterForm()
        return render(request, "register.html", {"form": form})
