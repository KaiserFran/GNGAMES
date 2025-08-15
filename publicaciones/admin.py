from django.contrib import admin
from .models import Publicacion, Comentario

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'usuario', 'categoria', 'fecha_creacion']

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['publicacion', 'usuario', 'fecha_creacion']