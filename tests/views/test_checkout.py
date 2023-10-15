import pytest
from django.test import Client
from store.models.customer import Customer
from store.models.product import Product
from store.models.category import Category
from store.views.checkout import CheckOut

@pytest.mark.django_db
def test_checkout_view():
    client = Client()
    response = client.post('/checkout/', {'address': '123 Main St', 'phone': '123-456-7890'})
    
    # Cliente temporal para la prueba
    customer = Customer.objects.create(first_name='John', last_name='Doe', email='john.doe@example.com')
    request = response.wsgi_request
    request.session['customer'] = customer.id

    # Carrito en la sesión y productos en la lista
    request.session['cart'] = {'1': 2, '2': 1}

    # productos de la base de datos y asócialos con una categoría
    category = Category.objects.create(name='Category 1')
    product1 = Product.objects.create(name='Product 1', price=10, category=category)
    product2 = Product.objects.create(name='Product 2', price=20, category=category)

    # Realizacion de la prueba
    response = CheckOut.as_view()(request)

    assert response.status_code == 302
    assert response.url == '/cart'
    