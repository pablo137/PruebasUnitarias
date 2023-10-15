import pytest
from store.models.category import Category
from store.models.customer import Customer
from store.models.orders import Order
from store.models.product import Product

# Fixture de configuración para la categoría
@pytest.fixture
def setup_test_order():
    categoria = Category.objects.create(
        name = 'Comida',
        image = 'uploads/categorias/img_defecto_hhgi4q.jpg',
    )
    customer = Customer.objects.create(first_name="John", last_name="Doe", phone="65555665", email="john@example.com", password="123", rol="Cliente")
    product = Product.objects.create(user=customer ,name="Abrigo", price=100, category=categoria, stock=True)
    yield categoria, customer, product
    
    # Limpieza después de las pruebas TIER DOWN
    product.delete()
    customer.delete()
    categoria.delete()

    

@pytest.mark.django_db
def test_placeOrder(setup_test_order):
    categoria, customer, product = setup_test_order
    order = Order.objects.create(customer=customer, product=product, quantity=2, price=200)
    order.placeOrder()
    # Verifica que la orden se haya guardado correctamente
    assert Order.objects.count() == 1

@pytest.mark.django_db
def test_get_orders_by_customer(setup_test_order):
    categoria, customer, product = setup_test_order
    order1 = Order.objects.create(customer=customer, product=product, quantity=2, price=200)
    order2 = Order.objects.create(customer=customer, product=product, quantity=3, price=300)

    orders = Order.get_orders_by_customer(customer.id)

    # Verifica que se recuperen las órdenes del cliente correcto y se ordenen por fecha
    assert len(orders) == 2
    assert orders[0].date >= orders[1].date

@pytest.mark.django_db
def test_order_str(setup_test_order):
    categoria, customer, product = setup_test_order
    order = Order.objects.create(customer=customer, product=product, quantity=2, price=200)

    expected_str = f"Producto: {product.name}, Precio: {order.price} Bs, Cantidad: {order.quantity}"
    assert str(order) == expected_str