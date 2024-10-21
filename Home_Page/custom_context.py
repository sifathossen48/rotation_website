from About_Page.models import Info
from Home_Page.models import Brand, Category, Industries, Product


def common_context(request):
    brands = Brand.objects.all()
    category = Category.objects.all()
    industries = Industries.objects.all()
    abouts = Info.objects.last()
    products = Product.objects.all()
    return {
        'brands': brands,
        'category': category,
        'industries': industries,
        'abouts': abouts,
        'products': products
    }