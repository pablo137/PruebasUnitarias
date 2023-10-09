import pytest
from store.models.category import Category

@pytest.mark.django_db
def test_category_str():
    categoria = Category.objects.create(
        name = 'Comida',
        image = 'uploads/categorias/img_defecto_hhgi4q.jpg',
    )
    assert categoria.__str__() == 'Comida'