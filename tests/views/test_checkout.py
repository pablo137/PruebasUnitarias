from django.test import TestCase
from django.test import Client
from store.models.customer import Customer
from store.models.product import Product
from store.models.category import Category
from store.views.checkout import CheckOut

class CheckoutViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        # Cliente temporal para la prueba
        self.customer = Customer.objects.create(first_name='John', last_name='Doe', email='john.doe@example.com')
        self.cart_data = {'1': 2, '2': 1}

        # Productos de la base de datos y asócialos con una categoría
        self.category = Category.objects.create(name='Category 1')
        self.product1 = Product.objects.create(name='Product 1', price=10, category=self.category)
        self.product2 = Product.objects.create(name='Product 2', price=20, category=self.category)

    def tearDown(self):
        # Limpia los objetos de prueba
        self.customer.delete()
        self.category.delete()
        self.product1.delete()
        self.product2.delete()

    def test_checkout_view(self):
        response = self.client.post('/checkout/', {'address': '123 Main St', 'phone': '123-456-7890'})
        request = response.wsgi_request
        request.session['customer'] = self.customer.id
        request.session['cart'] = self.cart_data

        # Realización de la prueba
        response = CheckOut.as_view()(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/cart')