from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class GameView(LoginRequiredMixin, TemplateView):
    template_name = 'game/index.html'
    login_url='/admin'
