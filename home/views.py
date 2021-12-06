from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = "myview.html"
    login_url = 'accounts/login.html'

# Create your views here.

class HomeView(TemplateView):
    template_name = "home/index.html"
    extra_content = {}


# def index(request):
#     return render(request, 'home/index.html', {})

def about(request):
    return render(request, 'home/about.html', {})