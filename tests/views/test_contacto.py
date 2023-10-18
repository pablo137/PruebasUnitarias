from audioop import reverse
from django.test import TestCase
from django.test import Client
from store.models.customer import Customer
from twilio.base.exceptions import TwilioRestException
from unittest.mock import patch  # Importa la biblioteca de mocks

class TwilioClientMock:
    @staticmethod
    def messages():
        return TwilioMessageMock()

class TwilioMessageMock:
    def create(self, from_, body, to):
        return {'sid': 'SMXXXXXXXXXXXXXXXXXXXXX'}


class ContactoTestCase(TestCase):
    def setUp(self):
        self.data = {
            'nombre': 'John Doe',
            'correo': 'john@example.com',
            'mensaje': 'Hola, este es un mensaje de prueba.'
        }
        self.client = Client()

        # Cliente temporal para la prueba
        self.customer = Customer.objects.create(first_name='John', last_name='Doe', email='john.doe@example.com')

    def tearDown(self):
        # Limpia los objetos de prueba
        self.customer.delete()

#test_Contacto
    def test_contacto_post_valid(self):
        # Prueba de solicitud POST válida a la vista 'contacto'
        response = self.client.post('/contacto', self.data)
        self.assertEqual(response.status_code, 302)  # Ajusta el código de estado según tu vista de redirección

#test_Contactanos
    @patch('store.views.contacto.Client')  # Usamos patch para reemplazar temporalmente Client
    def test_contactanos_post_valid(self, MockTwilioClient):
        data = {
            'mensaje': 'Este es un mensaje de prueba válido.'
        }

        # Crea una instancia de MockTwilioClient
        mock_client = MockTwilioClient.return_value
        mock_client.messages.create.return_value = {'sid': 'SMXXXXXXXXXXXXXXXXXXXXX'}

        # Simula un POST válido enviando el formulario con datos válidos
        response = self.client.post('/contactanos', data)

        # Agrega aserciones para verificar el comportamiento esperado
        self.assertEqual(response.status_code, 302)  # Verifica que se redirija
        
    def test_contactanos_post_error(self):
        data = {
            'mensaje': 'Este es un mensaje de prueba.'
        }

        with self.assertRaises(TwilioRestException):
            # Forzamos el error en Twilio
            with self.settings(TWILIO_AUTH_TOKEN='invalid_token'):
                response = self.client.post('/contactanos', data)