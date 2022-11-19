from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from .models import Testimonial, Product
from django.views.generic import View
from django.shortcuts import render
from django.conf import settings
from django.core import cache

decorators = [csrf_exempt]
is_production = not settings.DEBUG

if is_production:
    decorators = [csrf_exempt, cache_page(86400)]


@method_decorator(decorators, name="dispatch")
class ShopView(View):
    def get(self, request, *args, **kwargs):
        if is_production:
            products_cache_key = "products_cache_key"
            testimonials_cache_key = "testimonials_cache_key"

            products_cache_timeout = 86400
            testimonials_cache_timeout = 86400

            products = cache.get(products_cache_key)
            testimonials = cache.get(testimonials_cache_key)

            if not products:
                products = Product.objects.values()
                cache.set(products_cache_key, products, products_cache_timeout)

            if not testimonials:
                testimonials = Testimonial.objects.values()
                cache.set(testimonials_cache_key, testimonials, testimonials_cache_timeout)

        else:
            products = Product.objects.values()
            testimonials = Testimonial.objects.values()

        context = {
            "products": list(products),
            "testimonials": list(testimonials)
        }

        if is_production:
            return render(request, "shop/index_cache.html", context)

        return render(request, "shop/index.html", context)


def error_404_view(request, *args, **kwargs):
    return render(request, "shop/404.html")


def error_500_view(request, *args, **kwargs):
    return render(request, "shop/500.html")
