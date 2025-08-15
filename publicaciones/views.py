from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Publicacion
from .forms import PublicacionForm, ComentarioForm

def lista_publicaciones(request):
    categoria = request.GET.get('categoria')  # obtiene la categoría seleccionada del select
    if categoria:  # si se eligió una categoría
        publicaciones = Publicacion.objects.filter(categoria=categoria).order_by('-fecha_creacion')
    else:  # si no se eligió, mostramos todas
        publicaciones = Publicacion.objects.all().order_by('-fecha_creacion')
    
    return render(request, 'publicaciones/lista.html', {'publicaciones': publicaciones})
@login_required
def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.usuario = request.user
            publicacion.save()
            return redirect('lista_publicaciones')
    else:
        form = PublicacionForm()
    return render(request, 'publicaciones/crear.html', {'form': form})

@login_required
def editar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = PublicacionForm(request.POST, request.FILES, instance=publicacion)
        if form.is_valid():
            form.save()
            return redirect('lista_publicaciones')
    else:
        form = PublicacionForm(instance=publicacion)
    return render(request, 'publicaciones/editar.html', {'form': form})

@login_required
def borrar_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk, usuario=request.user)
    if request.method == 'POST':
        publicacion.delete()
        return redirect('lista_publicaciones')
    return render(request, 'publicaciones/borrar.html', {'publicacion': publicacion})

@login_required
def agregar_comentario(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.publicacion = publicacion
            comentario.save()
            return redirect('lista_publicaciones')
    else:
        form = ComentarioForm()
    return render(request, 'publicaciones/comentario.html', {'form': form, 'publicacion': publicacion})


def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    comentarios = publicacion.comentarios.all().order_by('-fecha_creacion')

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.publicacion = publicacion
            nuevo_comentario.usuario = request.user  # usuario logueado
            nuevo_comentario.save()
            return redirect('detalle_publicacion', pk=publicacion.pk)
    else:
        form = ComentarioForm()

    return render(request, 'publicaciones/detalle_publicacion.html', {
        'publicacion': publicacion,
        'comentarios': comentarios,
        'form': form
    })