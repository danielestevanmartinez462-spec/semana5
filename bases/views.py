from django.shortcuts import render, redirect, get_object_or_404
from .forms import AprendizForm
from .models import aprendiz
from django.contrib import messages

def listar_aprendices(request):
 aprendices = aprendiz.objects.all()
 return render(request, 'bases/lista_aprendiz.html', {'aprendices': aprendices})

def crear_aprendiz(request):
    if request.method == 'POST':
        form = AprendizForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_aprendices')
    else:
        form = AprendizForm()

    return render(request, 'bases/crear_aprendiz.html', {'form': form})

def editar_aprendiz(request, documento):
    aprendiz_obj = get_object_or_404(aprendiz, documento=documento)

    if request.method == 'POST':
        form = AprendizForm(request.POST, instance=aprendiz_obj)
    else:
        form = AprendizForm(instance=aprendiz_obj)

    form.fields['documento'].disabled = True

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Se editó de manera correcta')
        return redirect('listar_aprendices')

    return render(request, 'bases/crear_aprendiz.html', {
        'form': form,
        'titulo': f'Editar {aprendiz_obj.nombre} - {aprendiz_obj.apellido}',
    })

def eliminar_aprendiz(request ,documento ):
    aprendiz_objs = get_object_or_404(aprendiz, documento=documento)
    if request.method == 'POST':
        aprendiz_objs.delete()
        messages.success(request,'eliminar el usuario')
        return redirect('listar_aprendices')
     
    return render(request, 'bases/eliminar_aprendiz.html', {'aprendiz_objs': aprendiz_objs})


def buscar_aprendiz(request):
    resultado = None
    if request.method == 'POST':
        documento = request.POST.get('documento', '').strip()
        resultado = aprendiz.objects.filter(documento=documento).first()
        if resultado is None:
            messages.error(request, f'No se encontró ningún aprendiz con el documento {documento}.')

    return render(request, 'bases/buscar.html', {'aprendiz': resultado})


def mapa(request):
    return render(request, 'bases/mapa.html')