from datetime import datetime, date
from dominio.turno import Turno

def modificar_turno_primera_parte(servicio):
    while True:
        #Permite introducir el ID_TURNO a modificar, ademas muestra los turnos con los diferentes estas -> activo, confirmado.
        
        print("\n== Modificar turno ==\n")
        print("1. Para ingresar el ID del turno\n2. Ver turnos ACTIVOS\n3. Ver turnos CONFIRMADOS\n4. Ver TODOS los turnos (excepto cancelados)\n0. Salir\n")

        try:
            opcion_turnero = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Ingrese una opcion correcta (0-1-2-3-4)")
            continue           
          
        if opcion_turnero == 1:  
            id_ingresado = ingresar_turno_y_validar(servicio)
            print("\n== Modificar turno ==\n")

            turno = servicio.instanciar_turno_por_id(id_ingresado)
            print(f'Usted ingreso el ID_TURNO: {turno.id_turno}')
            
            #SEGUNDA PARTE DE LA OPCION UPDATE.
            modificar_turno_segunda_parte(servicio,turno)
        
        elif opcion_turnero == 2:
            print("\n== TURNOS ACTIVOS ==\n")
            ver_turno_estado(servicio,"activo") 
        
        elif opcion_turnero == 3:
            print("\n== TURNOS CONFIRMADOS ==\n")
            ver_turno_estado(servicio,"confirmado")
        
        elif opcion_turnero == 4:
            print("\n== TURNOS ACTIVOS Y CONFIRMADOS ==\n")
            ver_turno_estado(servicio,"activo")
            ver_turno_estado(servicio,"confirmado")
            #Aca se puede agregar la misma funcion con el estado "cancelado" y permitiria verlos.
            #No se hace porque confirmar turnos cancelados, puede romper el sistema.
 
        elif opcion_turnero == 0:
            break
        
        else:
            print("Ingrese una opcion valida")
        
def modificar_turno_segunda_parte(servicio,turno):
    # Segunda parte de modificar. Permite confirmar, cancelar, reprogramar turnos y cambiarlo de equipo
    while True:   
        print("\n1. Confirmar turno\n2. Cancelar turno\n3. Reprogramar turno\n0. Salir")
        try:
            menu_principal = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Ingrese una opcion correcta (0-1-2-3-4-0)")
            continue
        
        if menu_principal == 1:
            modificar_turno(servicio,"confirmar","confirmado",turno)
            break
        
        elif menu_principal == 2:
            modificar_turno(servicio,"cancelar","cancelado",turno)
            break
        
        elif menu_principal == 3:
            reprogramar_turno(servicio,turno)
            print("\n==Informacion del nuevo turno==")
            servicio.informacion_turno_por_id_turno(turno.id_turno)
        
        elif menu_principal == 0:
            break
        
        else:
            print("Ingrese una opcion valida")
            
            
def ingresar_turno_y_validar(servicio):
    #Cumple la primera parte de la funcion modificar turno. Solicita ID 
    try:
        id_turno_a_modificar = int(input("Ingrese el ID del turno que quiere modificar: "))
    except ValueError:
        print("El id debe ser un numero")
    return id_turno_a_modificar
        
 
       
def reprogramar_turno(servicio, turno: Turno):
    while True:
       try:
           print("== Esta seguro que desea reprogramar el turno? ==\n1. Si\n2. No")
           confirmacion = int(input("Ingrese una opcion: "))
       except ValueError:
           print("Ingrese una opcion correcta")
           continue
       if confirmacion == 1:
            nombre_equipo = servicio.nombre_equipo(turno.id_resonador)
            print(F'==Informacion actual del turno==\nFecha: {turno.fecha_hora}\nEquipo: {nombre_equipo} ')
            
            fecha_hora_nueva, resonador_nuevo = pedir_nuevos_datos_turno(servicio, turno)
            
            try:
               actualizacion = servicio.reprogramar_turno(turno.id_turno,fecha_hora_nueva,resonador_nuevo)
               if actualizacion:
                    print("\nTurno actualizado con exito")
                    return
            except ValueError as e:
                print(f'Error al reprogramar: {e}')

       elif confirmacion == 2:
           break
       else: 
           print("Ingrese 1 o 2")
           
def pedir_nuevos_datos_turno(servicio, turno_actual):
    fecha_hora_final = turno_actual.fecha_hora
    resonador_final = turno_actual.id_resonador
    
    while True:
        print("\n1. Nueva fecha\n2. Nueva hora\n3. Nuevo equipo\n0.Salir y confirmar modificacion")
        try:
            opcion = int(input('Ingrese una opcion: '))
        except ValueError:
            print("Ingrese una opcion valida (1-2-3-0)")
            continue
               
        if opcion == 1:
            print("Ingrese la nueva fecha")
            
            try:
                fecha_str = input("Fecha (YYYY-MM-DD): ")
            except ValueError:
                print("Ingrese una fecha con el formato correcto")
            nueva_fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
            fecha_hora_final = datetime.combine(nueva_fecha, fecha_hora_final.time())
            print("Fecha actualizada")
                
        elif opcion == 2:
            print("IMPORTANTE: Los turnos se registran CADA 30 MINUTOS")
            print("Horarios permitidos: :00 o :30 (Ejemplos: 09:00, 09:30, 10:00, etc.)")
            print("Los turnos solo pueden ser entre las 08:00 y 20:00hs")
            try:
                hora_str = input("Hora (HH:MM): ")
            except ValueError:
                print(("Ingrese una hora con el formato correcto (HH:MM)"))
            nueva_hora = datetime.strptime(hora_str, "%H:%M").time()
            fecha_hora_final = datetime.combine(fecha_hora_final.date(),nueva_hora)
        elif opcion == 3:
            print("En que resonador desea registrar el turno? \n1. Resonador 1.5#1\n2. Resonador 1.5#2\n3. Resonador 3T")
            try:
                nuevo_resonador = int(input("Ingrese el resonador que desea: "))
                if nuevo_resonador in [1, 2, 3]:
                    resonador_final = nuevo_resonador
            except ValueError:
                print("Ingrese una opcion valida")
                
        elif opcion == 0:
            return fecha_hora_final, resonador_final
        else:
            print("Ingrese una opcion valida")

def cambiar_equipo(servicio, turno: Turno):
    while True:
        try:
            print("== Esta seguro que desea cambiar de equipo? ==\n1. Si\n2. No")
            confirmacion = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Ingrese una opcion correcta")
            continue
        if confirmacion == 1:
            print("En que resonador desea registrar el turno? \n1. Resonador 1.5#1\n2. Resonador 1.5#2\n3. Resonador 3T")
            try:
                id_resonador = int(input("Ingrese el resonador que desea: "))
            except ValueError:
                print("Debe ingresar un numero")

            
            servicio.cambiar_equipo(turno,id_resonador)
        
        elif confirmacion == 2:
            break
        else:
            print("Ingrese 1 o 2")
        
            

def modificar_turno(servicio,accion, estado ,turno : Turno):
    #Accion es lo que se desea hacer -> confirmar o cancelar el turno
    #estado es el nuevo estado del turno -> confirmado o cancelado
    
    while True:
        try:
            print(f"== Esta seguro que desea {accion} el turno? ==\n1. Si\n2. No")
            confirmacion = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Ingrese una opcion correcta")
            continue
        if confirmacion == 1:
            try:
                turno_estado = estado
                servicio.modificar_estado_turno(turno,turno_estado)
            except ValueError as e:
                print(e)
            break
        elif confirmacion == 2:
            break
                

def ver_turno_estado(servicio,estado):
    turnos_confirmados = servicio.mostrar_id_turnos_estados(estado) 
    for turno in  turnos_confirmados:
        print(f'ID_Turno: {turno[0]}, Estudio: {turno[1]}, Nombre: {turno[2]} {turno[3]}, Estado: {turno[4]}')
    return    
