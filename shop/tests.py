from django.test import Client, TestCase
from django.urls import reverse
from .models import Product, Category

class ShopModelTests(TestCase):
    def setUp(self):
        self.c = Category.objects.create(name='Hot sneakers')
        self.product = Product.objects.create(name='Jordan 4 Black Cat', category=self.c,stock='25', price='300.00')

    def test_product_listing(self):
        self.assertEqual(f'{self.product.price}','300.00')
        self.assertEqual(f'{self.product.name}', 'Jordan 4 Black Cat')
        self.assertEqual(f'{self.product. stock}', '25')

    def test_product_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'Hot sneakers')
        self.assertTemplateUsed(response, 'category.html', 'home.html', 'base.html')

    def test_product_detail_view(self):
        response = self.client.get(self.product.get_absolute_url()) 
        no_response = self.client.get('/1/1/')
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(no_response.status_code, 404) 
        self.assertContains (response, 'Jordan 4 Black Cat')
        self.assertTemplateUsed (response, 'products.html' ,'base.html')



# class ProductTests(TestCase):
#     def setUp(self):
#         self.Product = Product.objects.create(
#             name='Test',
#             description='Testing of product',
#             image=''
#         )
#     def test_Product_listing(self):
#         self.assertEqual(f'{self.Product.name}', 'Test')
#         self.assertEqual(f'{self.Product.description}', 'Testing of product')
#         self.assertEqual(f'{self.Product.image}', '')
#         self.assertEqual(f'{self.Product.price}', '111')
#         self.assertEqual(f'{self.Product.stock}', '10')
#         self.assertEqual(f'{self.Product.available}', 'True')