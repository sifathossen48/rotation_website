from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/',include('News_Page.urls')),
    path('contact/',include('Contact_Page.urls')),
   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

