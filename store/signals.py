from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.customer import Customer

@receiver(post_save, sender=Customer)
def asignar_rol_cliente(sender, instance, created, **kwargs):
    if created:
        instance.rol = 'cliente'
        instance.save()