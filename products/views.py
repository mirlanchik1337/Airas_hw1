from django.shortcuts import render
from products.models import Product


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        posts = Product.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'products/products.html', context=context)