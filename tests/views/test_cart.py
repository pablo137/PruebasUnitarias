from django.test import TestCase
from django.urls import reverse
import pytest
from store.models import Product
from django.contrib.sessions.middleware import SessionMiddleware

# @pytest.mark.django_db
# class CartViewTestCase(TestCase):
#     def setUp(self):
#         # Configura datos de prueba, como productos en el carrito en la sesión
#         self.product1 = Product.objects.create(name="Product 1", price=10.00)
#         self.product2 = Product.objects.create(name="Product 2", price=15.00)
#         self.client.session['cart'] = {self.product1.id: 1, self.product2.id: 2}
#         self.client.session.save()

#     def test_cart_view(self):
#         # Simula una solicitud GET a la vista "Cart"
#         request = self.client.get(reverse('cart'))  # Asegúrate de reemplazar 'cart' con la URL real de tu vista

#         # Verifica que la vista responda con un código 200 (éxito)
#         self.assertEqual(request.status_code, 200)

#         # Verifica que los productos se pasen al contexto y se muestren en la respuesta
#         self.assertQuerysetEqual(request.context['products'], [repr(self.product1), repr(self.product2)])

#     def tearDown(self):
#         # Limpia la sesión después de la prueba
#         self.client.session.flush()