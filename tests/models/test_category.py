import pytest
from django.test import TestCase
from store.models.category import Category
@pytest.mark.django_db
class test_category(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test comida")
    
    def test_get_all_categories(self):
        categories = Category.get_all_categories()
        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0].name, "Test comida")

    def test_category_str(self):
        self.assertEqual(str(self.category), "Test comida")
