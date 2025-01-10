from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Campista, Reserva

# Página de inicio
def inicio(request):
    return render(request, 'inicio.html')
# ====================== Campista ======================
# Mostrar formulario para crear un nuevo campista
def nuevo_campista(request):
    return render(request, 'campista.html')  
# Mostrar formulario para listar campistas
def listar_campista(request):
    campistas=Campista.objects.all()
    return render(request, 'listadoCampista.html', {'campistas': campistas})

#===========================GUARDAR CAMPISTA=====================
def guardar_campista(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombres = request.POST.get('txt_nombre')
        correo = request.POST.get('txt_correo')
        telefono = request.POST.get('txt_telefono')
        direccion = request.POST.get('txt_direccion')

        # Validar que los campos obligatorios no estén vacíos
        if not nombres or not correo or not telefono:
            messages.error(request, "Por favor, completa todos los campos obligatorios.")
            return redirect('nuevo_campista')
        
        # Crear el nuevo campista y guardarlo en la base de datos
        Campista.objects.create(
            nombres=nombres,
            correo=correo,
            telefono=telefono,
            direccion=direccion
        )
        messages.success(request, "Campista agregado correctamente.")
        return redirect('listar_campista')
    else:
        # Si no es una solicitud POST, redirige a la página de nuevo campista
        return redirect('nuevo_campista')

# Eliminar un campista por ID
def eliminar_campista(request, id):
    campista = get_object_or_404(Campista, id=id)
    campista.delete()
    messages.success(request, "Campista eliminado correctamente.")
    return redirect('listar_campista')

#FUNCION PARA MOSTRAR EL FORMULARIO DE EDICION
def editar_campista(request,id):
    campista=Campista.objects.get(id=id) #esto seria un tipo select * from
    return render(request,"editarCampista.html" , {'campista':campista})

#FUNCION PARA CONFIRMAR LOS CAMBIOS DE CAMPISTA

def edicion_campista(request,id):
    campista = Campista.objects.get(id=id)
    nombres = request.POST['txt_nombre']
    correo = request.POST['txt_correo']
    telefono = request.POST['txt_telefono']
    direccion = request.POST['txt_direccion']

    campista.nombres=nombres
    campista.correo=correo
    campista.telefono=telefono
    campista.direccion=direccion
    campista.save()

    messages.success(request, "Campista Editado Exitosamente")
    return redirect('/listadoCampista')



#====================================VIEWS DE RESERVA========================================0
# Formulario de nueva reserva
def nuevo_reserva(request):
    campistas = Campista.objects.all()  # Obtener todos los campistas
    return render(request, 'reserva.html', {'campistas': campistas})
#listar reserva
def listar_reserva(request):
    reserva=Reserva.objects.all()
    return render(request, 'listadoReserva.html', {'reserva': reserva})
#guardar reserva
def guardar_reserva(request):
    if request.method == 'POST':
        fecha_inicio = request.POST['txt_fechainicio']
        fecha_fin = request.POST['txt_fechafin']
        campista_id = request.POST['txt_campista']
        tipo_alojamiento = request.POST['txt_alojamiento']
        numero_personas = request.POST['txt_numero']
        estado_reserva = request.POST['txt_estadoR']
        observaciones = request.POST.get('txt_observaciones', '')

        campista = get_object_or_404(Campista, id=campista_id)
        nueva_reserva = Reserva(
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            campista=campista,
            tipo_alojamiento=tipo_alojamiento,
            numero_personas=numero_personas,
            estado_reserva=estado_reserva,
            observaciones=observaciones
        )
        nueva_reserva.save()
        return redirect('listar_reserva')
    return redirect('nuevo_reserva')

#eliminar resrrva
def eliminar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('listar_reserva')

#editar reserva
def editar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    campistas = Campista.objects.all()
    return render(request, 'editarReserva.html', {'reserva': reserva, 'campistas':campistas})

# Guardar cambios de edición
def edicion_reserva(request, id):
    if request.method == 'POST':
        reserva = get_object_or_404(Reserva, id=id)
        reserva.fecha_inicio = request.POST['txt_fechainicio']
        reserva.fecha_fin = request.POST['txt_fechafin']
        campista_id = request.POST['txt_campista']
        reserva.campista = get_object_or_404(Campista, id=campista_id)
        reserva.tipo_alojamiento = request.POST['txt_alojamiento']
        reserva.numero_personas = request.POST['txt_numero']
        reserva.estado_reserva = request.POST['txt_estadoR']
        reserva.observaciones = request.POST.get('txt_observaciones', '')
        reserva.save()
        return redirect('listar_reserva')
    return redirect('listar_reserva')