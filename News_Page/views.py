from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from News_Page.models import News, NewsGallery

# Create your views here.
class NewsView(TemplateView):
    template_name = 'news.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all()
        return context
class NewsDetailView(View):
    def get(self, request, n_id):
        n = News.objects.get(id=n_id)
        context = {
            'n': n,
            'news': News.objects.all(),
            'newsGallery': NewsGallery.objects.all()
          
        }
        return render(request, 'news-single.html', context=context)