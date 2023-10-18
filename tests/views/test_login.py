from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from store.views.login import Login, logout
from unittest.mock import patch

class LoginTestCase(TestCase):
    def setUp(self):
        # Crear un cliente de prueba con contraseña encriptada
        self.customer = Customer.objects.create(
            email="test@example.com",
            password=make_password("testpassword")
        )

    def test_login_view_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_view_post_valid_credentials(self):
        data = {
            'email': 'test@example.com',
            'password': 'testpassword',
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 302)  # Redirección exitosa
        # Asegurarse de que el cliente esté en la sesión
        self.assertEqual(self.client.session['customer'], self.customer.id)

    def test_login_view_post_invalid_credentials(self):
        data = {
            'email': 'test@example.com',
            'password': 'wrongpassword',
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 200)  # Debe permanecer en la página de inicio de sesión
        self.assertContains(response, 'Email or Password invalid !!')

    def test_login_view_with_invalid_customer(self):
        # Configura un caso en el que Customer.get_customer_by_email devuelve None
        with patch('store.models.customer.Customer.get_customer_by_email') as mock_get_customer:
            mock_get_customer.return_value = None
            data = {
                'email': 'nonexistent@example.com',
                'password': 'somepassword',
            }
            response = self.client.post(reverse('login'), data)
            self.assertEqual(response.status_code, 200)
            # Asegurarse de que se muestra el mensaje de error
            self.assertContains(response, 'Email or Password invalid !!')    

class LogoutTestCase(TestCase):
    def test_logout_view(self):
        # Iniciar sesión primero
        self.client.session['customer'] = 1
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirección exitosa
        self.assertNotIn('customer', self.client.session)
