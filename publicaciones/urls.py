from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_publicaciones, name='lista_publicaciones'),
    path('crear/', views.crear_publicacion, name='crear_publicacion'),
    path('editar/<int:pk>/', views.editar_publicacion, name='editar_publicacion'),
    path('borrar/<int:pk>/', views.borrar_publicacion, name='borrar_publicacion'),
    path('comentario/<int:pk>/', views.agregar_comentario, name='agregar_comentario'),
    path('publicacion/<int:pk>/', views.detalle_publicacion, name='detalle_publicacion'),
]

