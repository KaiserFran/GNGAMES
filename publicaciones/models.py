from django.db import models
from django.conf import settings

class Publicacion(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='publicaciones/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    CATEGORIAS = [
            ('ACC', 'Acción'),
            ('TER', 'Terror'),
            ('AVN', 'Aventura'),
            ('CAR', 'Carreras'),
            ('DIV', 'Diversión'),
            ('MAB', 'Mundo Abierto'),
            ('SHO', 'Shooter'),
            ('MUL', 'Multijugador'),
            ('PEL', 'Pelea'),
            ('OTR', 'Otros'),
        ]
    categoria = models.CharField(max_length=3, choices=CATEGORIAS, default='OTR')
    
def __str__(self):
    return f"{self.titulo} - {self.get_categoria_display()}"
    

class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username}: {self.texto[:20]}"
