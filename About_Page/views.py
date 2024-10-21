from django.shortcuts import render
from django.views.generic import TemplateView

from About_Page.models import Director
# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['directors'] = Director.objects.all()
        return context