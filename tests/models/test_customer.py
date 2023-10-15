import pytest
from store.models.customer import Customer

@pytest.mark.django_db
def test_customer_creation():
    customer = Customer(
        first_name="John",
        last_name="Doe",
        phone="1234567890",
        email="john@example.com",
        password="password123",
        rol="cliente",
    )
    customer.register()
    assert Customer.objects.count() == 1

@pytest.mark.django_db
def test_get_customer_by_email():
    customer = Customer(
        first_name="Jane",
        last_name="Smith",
        phone="9876543210",
        email="jane@example.com",
        password="password456",
        rol="emprendedor",
    )
    customer.register()
    retrieved_customer = Customer.get_customer_by_email("jane@example.com")
    assert retrieved_customer.email == "jane@example.com"

@pytest.mark.django_db
def test_get_customer_by_nonexistent_email():
    retrieved_customer = Customer.get_customer_by_email("nonexistent@example.com")
    assert retrieved_customer is None

@pytest.mark.django_db
def test_is_exists():
    customer = Customer(
        first_name="Alice",
        last_name="Johnson",
        phone="5555555555",
        email="alice@example.com",
        password="password789",
        rol="todoenuno",
    )
    customer.register()

    assert customer.isExists()
    assert not Customer(email="nonexistent@example.com").isExists()

@pytest.mark.django_db
def test_customer_str_method():
    customer = Customer(
        first_name="Bob",
        last_name="Brown",
        phone="1231231234",
        email="bob@example.com",
        password="password123",
        rol="cliente",
    )
    assert str(customer) == "Bob Brown"