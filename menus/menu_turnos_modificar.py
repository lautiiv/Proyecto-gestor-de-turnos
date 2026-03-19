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
            pass
            
       elif confirmacion == 2:
           break
       else: 
           print("Ingrese 1 o 2")

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
