from django.test import TestCase, Client
from store.models.customer import Customer
from django.urls import reverse

class SignupViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.valid_data = {
            'firstname': 'John',
            'lastname': 'Doe',
            'phone': '1234567890',
            'email': 'john@example.com',
            'password': 'secretpassword',
        }
    
    def tearDown(self):
        # Limpia los objetos de prueba, si es necesario
        Customer.objects.filter(email=self.valid_data['email']).delete()


    def test_signup_get(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')


    def test_signup_post_invalid_data(self):
        response = self.client.post(self.signup_url, data=self.valid_data, follow=True)
        self.assertEqual(response.status_code, 200)
        # # Verificar que el usuario se haya registrado en la base de datos
        self.assertFalse(Customer.objects.filter(email=self.valid_data['email']).exists())


    def test_signup_post_invalid_name(self):
        invalid_data = {
            'firstname': '',
            'lastname': 'Doe',
            'phone': '12345',
            'email': 'invalid-email',
            'password': 'short',
        }
        response = self.client.post(self.signup_url, data=invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Primer nombre es requerido!!')

    def test_signup_post_invalid_name_more_4_char(self):
        invalid_data = {
            'firstname': 'Jo',
            'lastname': '',
            'phone': '12345',
            'email': 'invalid-email',
            'password': 'short',
        }
        response = self.client.post(self.signup_url, data=invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Primer nombre deberia tener al menos 4 o mas caracteres ')

    def test_signup_post_invalid_last_name(self):
        invalid_data = {
            'firstname': 'Michael',
            'lastname': '',
            'phone': '12345',
            'email': 'invalid-email',
            'password': 'short',
        }
        response = self.client.post(self.signup_url, data=invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'El apellido es requerido')

    def test_signup_post_invalid_phone(self):
        invalid_data = {
            'firstname': 'Michael',
            'lastname': 'Doekel',
            'phone': '',
            'email': 'invalid-email',
            'password': 'short',
        }
        response = self.client.post(self.signup_url, data=invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'El telefono es requerido')

    def test_signup_post_invalid_phone_more_10_num(self):
        invalid_data = {
            'firstname': 'Michael',
            'lastname': 'Doekel',
            'phone': '12',
            'email': 'invalid-email',
            'password': 'short',
        }
        response = self.client.post(self.signup_url, data=invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'El telefono debe tener al menos 10 caracteres')

    def test_signup_post_invalid_password_more_6_char(self):
        invalid_data = {
            'firstname': 'Michael',
            'lastname': 'Doekel',
            'phone': '777755555666',
            'email': 'p481041231234@gmail.com',
            'password': 'short',
        }
        response = self.client.post(self.signup_url, data=invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'La contraseña debe tener al menos 6 caracteres')
