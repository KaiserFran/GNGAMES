from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    foto_perfil = models.ImageField(null=True, blank=True, upload_to='fotos/')

    def __str__(self):
        return self.username