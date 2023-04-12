import logging
from django.shortcuts import render

from shop.models import Product

logger = logging.getLogger(__name__)


def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})
