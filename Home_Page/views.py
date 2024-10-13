from django.shortcuts import render
from django.views.generic import TemplateView

from Home_Page.models import Brand, Client, Industries, Slider


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = Slider.objects.all()
        context['brands'] = Brand.objects.all()
        context['industries'] = Industries.objects.all()
        context['clients'] = Client.objects.all()
        return context
class IndustriesView(TemplateView):
    template_name = 'industries.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['industries'] = Industries.objects.all()
        return context