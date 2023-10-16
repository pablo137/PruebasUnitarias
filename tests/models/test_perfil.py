import pytest
from django.test import TestCase, Client
from store.models.customer import Customer
from store.models.perfil import UserProfile

@pytest.mark.django_db
class TestUserProfile(TestCase):
    def setUp(self):
        self.client = Client()

        # Crear un cliente temporal para la prueba
        self.customer = Customer.objects.create(
            first_name='Alice',
            last_name='Smith',
            phone='9876543210',
            email='alice@example.com',
            password='topsecret')

        # Obtener o crear el perfil del cliente
        self.perfil, created = UserProfile.objects.get_or_create(user=self.customer, defaults={'bio': 'Test bio'})

    def tearDown(self):
        self.customer.delete()
        self.perfil.delete()

    def test_userprofile_str(self):
        self.assertEqual(str(self.perfil), 'Perfil de: Alice Smith')