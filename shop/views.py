from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.views.generic import ListView, DetailView

# Create your views here.

class ProductCat(ListView):
    model = Product

    def get(self, request, category_id = None):
        category = None
        products = None

        if category_id != None:
            category = get_object_or_404(Category, id = category_id)
            products = Product.objects.filter(category = category, available = True)
        else:
            products = Product.objects.all().filter(available = True)

        paginator = Paginator(products, 8)
        try:
            Page = int(request.GET.get('page','1'))
        except:
            Page = 1
        try:
            products = paginator.page(Page)
        except(EmptyPage,InvalidPage):
            products = paginator.page(paginator.num_pages)

        return render(request, "category.html", {'category':category, 'products':products})

class ProdDetail(DetailView):
    model = Product

    def get(self, request, category_id, product_id):
        try:
            product = Product.objects.get(category_id = category_id, id = product_id)
        except Exception as e:
            raise e
        return render(request, "products.html", {'product':product})    