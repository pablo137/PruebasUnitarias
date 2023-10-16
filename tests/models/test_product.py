from django.test import TestCase
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer

class ProductModelTestCase(TestCase):
    def setUp(self):
        # Crea objetos de prueba necesarios para las pruebas
        self.category = Category.objects.create(name='Category 1')
        self.customer = Customer.objects.create(first_name='John', last_name='Doe', email='john.doe@example.com')
        self.product1 = Product.objects.create(name='Product 1', price=10, category=self.category, user=self.customer)
        self.product2 = Product.objects.create(name='Product 2', price=20, category=self.category, user=self.customer)

    def tearDown(self):
        # Limpia los objetos de prueba
        self.category.delete()
        self.customer.delete()
        self.product1.delete()
        self.product2.delete()
        
#test_get_all_products
    def test_get_all_products(self):
        products = Product.get_all_products()
        self.assertEqual(products.count(), 2)
        self.assertIn(self.product1, products)
        self.assertIn(self.product2, products)

#test_get_all_products_by_categoryid
    def test_get_all_products_by_categoryid(self):
        products = Product.get_all_products_by_categoryid(self.category.id)
        self.assertEqual(products.count(), 2)
        self.assertIn(self.product1, products)
        self.assertIn(self.product2, products)

    def test_get_all_products_by_categoryid_with_none_category(self):
        products = Product.get_all_products_by_categoryid(None)
        self.assertEqual(products.count(), 2)
        self.assertIn(self.product1, products)
        self.assertIn(self.product2, products)