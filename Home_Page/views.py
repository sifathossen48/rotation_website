from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from Home_Page.models import  Brand, Client, Slider


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = Slider.objects.all()
        context['clients'] = Client.objects.all()
        return context
class IndustriesView(TemplateView):
    template_name = 'industries.html'

def brand_detail(request, pk):
    # Get the brand by its primary key (pk)
    brand = get_object_or_404(Brand, pk=pk)
    return render(request, 'dodge-bearings.html', {
        'brand': brand,
    
    })