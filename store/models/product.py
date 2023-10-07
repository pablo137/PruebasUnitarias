from django.db import models
from .category import Category
from .customer import Customer


class Product(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, verbose_name='Nombre de producto')
    price = models.IntegerField(default=0, verbose_name='Precio')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, verbose_name='Categoria')
    description = models.TextField(max_length=200, default='' , blank=True, verbose_name='Descripcion')
    image = models.ImageField(default='uploads/products/img_defecto_p_fugbfc.jpg',upload_to='media/uploads/products/', verbose_name='Imagen de producto')
    stock = models.BooleanField(default=True, verbose_name='Estado')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()