from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Index(LoginRequiredMixin,TemplateView):
    login_url = '/accounts/user_login/'
    template_name = "index.html"
