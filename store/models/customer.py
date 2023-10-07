from django.db import  models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ObjectDoesNotExist

class Customer(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Nombre')
    last_name = models.CharField(max_length=50, verbose_name='Apellidos')
    phone = models.CharField(max_length=15, verbose_name='Telefono')
    email = models.EmailField(verbose_name='Correo')
    password = models.CharField(max_length=500, verbose_name='Password')
    ROL_CHOICES = (
        ('cliente', 'Cliente'),
        ('emprendedor', 'Emprendedor'),
        ('todoenuno', 'TodoEnUno'),
    )
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='cliente')


    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["first_name"]

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except ObjectDoesNotExist:
            return None


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return  False

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name