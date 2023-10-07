from django.db import  models

class Category(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(default='uploads/categorias/img_defecto_hhgi4q.jpg', upload_to='media/uploads/categorias/', verbose_name='Imagen de categoria')

    @staticmethod
    def get_all_categories():
        return Category.objects.all()


    def __str__(self):
        return self.name
