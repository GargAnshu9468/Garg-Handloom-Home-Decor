from .models import Testimonial, Product
from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "category"]


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "message"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
