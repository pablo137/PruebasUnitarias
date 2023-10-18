from django.test import TestCase
from django.test import Client
from store.models.customer import Customer
from store.models.orders import Order
from store.models.product import Product
from store.views.orders import OrderView

class OrderViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        # Cliente temporal para la prueba
        self.customer = Customer.objects.create(first_name='John', last_name='Doe', email='john.doe@example.com')

        # Productos de prueba
        self.product1 = Product.objects.create(name='Product 1', price=10)
        self.product2 = Product.objects.create(name='Product 2', price=20)

        # Órdenes de prueba
        self.order1 = Order.objects.create(product=self.product1, customer=self.customer, quantity=2, price=20, address='123 Main St', phone='123-456-7890', status=False)
        self.order2 = Order.objects.create(product=self.product2, customer=self.customer, quantity=1, price=20, address='456 Oak St', phone='987-654-3210', status=True)

    def tearDown(self):
        # Limpia los objetos de prueba
        self.customer.delete()
        self.product1.delete()
        self.product2.delete()
        self.order1.delete()
        self.order2.delete()

    def test_order_get(self):
        response = self.client.get('/orders/')
        request = response.wsgi_request
        request.session['customer'] = self.customer.id

        # Realización de la prueba
        response = OrderView.as_view()(request)

        self.assertEqual(response.status_code, 200)  # Ajusta el código de estado según tu vista
        # Verifica que los productos estan asignados a las ordenes
        self.assertContains(response, 'Product 1') 
        self.assertContains(response, 'Product 2')  
