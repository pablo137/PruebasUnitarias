import pytest
from django.core.exceptions import ObjectDoesNotExist
from store.models.customer import Customer

@pytest.mark.django_db
def test_crear_customer():
    customer = Customer.objects.create(
        first_name = 'Fabi',
        last_name = 'Copa',
        phone = '77606087',
        email = 'qchuchas1@gmail.com',
        password = '12345678901Au',
        rol = 'cliente',
    )
    assert customer.rol == 'cliente'