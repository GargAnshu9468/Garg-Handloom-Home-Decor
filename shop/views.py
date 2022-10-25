from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Testimonial, Product
from django.views.generic import View
from django.shortcuts import render


@method_decorator(csrf_exempt, name="dispatch")
class ShopView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.values()
        testimonials = Testimonial.objects.values()

        context = {
            "products": list(products),
            "testimonials": list(testimonials)
        }

        return render(request, "shop/index.html", context)


def error_404_view(request, *args, **kwargs):
    return render(request, "shop/404.html")


def error_500_view(request, *args, **kwargs):
    return render(request, "shop/500.html")
