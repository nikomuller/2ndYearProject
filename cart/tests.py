from django.test import TestCase, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from unittest.mock import MagicMock
from django.urls import reverse
from shop.models import Product, Category
from .models import Cart, CartItem
from .views import add_cart

class AddCartViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        request = self.factory.get('/')
        get_response = MagicMock()
        self.session_middleware = SessionMiddleware(get_response)
        response = self.session_middleware(request)

        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(name='Test Product', category=self.category, price=20, stock=30)
        self.cart = Cart.objects.create()
        self.cart_item1 = CartItem.objects.create(product=self.product, cart=self.cart, quantity=5) 
        self.cart_item2 = CartItem.objects.create(product=self.product, cart=self.cart, quantity=5)

    def test_add_cart_view(self):
        request = self.factory.post(reverse('cart:add_cart', args = [self.product.id]))
        self.session_middleware.process_request(request)
        request.session.save()
        response = add_cart(request, self.product.id)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(CartItem.objects.filter(cart=self.cart)), 2 )

    def tearDown(self):
        self.category.delete()
        self.product.delete()
        self.cart.delete()
        self.cart_item1.delete()
        self.cart_item2.delete() 
