import logging
from django.shortcuts import render

from shop.models import Product

logger = logging.getLogger(__name__)


def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "product_details.html", {"product": product})
