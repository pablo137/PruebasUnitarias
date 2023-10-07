from django.db import models
from .customer import Customer
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    img = models.ImageField(default='uploads/users/img_defecto_u_ruk6ou.jpg',upload_to='media/uploads/users/', verbose_name='Imagen de perfil')
    bio = models.TextField(blank=True, verbose_name='Biografia')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ["user"]

    def __str__(self) -> str:
        return "Perfil de: {0} {1}".format(self.user.first_name, self.user.last_name)

@receiver(post_save, sender=Customer)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=Customer)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


