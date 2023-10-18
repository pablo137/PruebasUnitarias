from django.test import TestCase
from django.test import Client
from store.models.customer import Customer
from store.models.perfil import UserProfile
from store.models.product import Product
from store.models.category import Category
from store.views.perfil import view_profile, edit_profile

class CheckoutViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        # Cliente temporal para la prueba
        self.customer = Customer.objects.create(first_name='John', last_name='Doe', email='john.doe@example.com')

    def tearDown(self):
        # Limpia los objetos de prueba
        self.customer.delete()


    def test_view_profile(self):
        response = self.client.get('/perfil/')
        request = response.wsgi_request
        request.session['customer'] = self.customer.id

        # Realización de la prueba
        response = view_profile(request)

        self.assertEqual(response.status_code, 200)

    def test_edit_profile(self):
        data = {
            'img': 'new_profile.jpg',
            'bio': 'Updated bio text',
        }
        response = self.client.post('/perfil/edit/', data)
        request = response.wsgi_request
        request.session['customer'] = self.customer.id

        # Realización de la prueba
        response = edit_profile(request)

        self.assertEqual(response.status_code, 200)
    