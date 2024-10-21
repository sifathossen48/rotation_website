from django.contrib import admin

from Home_Page.models import Brand, Category, Client, Gallery, Industries, Product, Slider

# Register your models here.
admin.site.register(Slider)
admin.site.register(Brand)
admin.site.register(Industries)
admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Gallery)