from django.contrib import admin

from Home_Page.models import Brand, Client, Industries, Slider

# Register your models here.
admin.site.register(Slider)
admin.site.register(Brand)
admin.site.register(Industries)
admin.site.register(Client)