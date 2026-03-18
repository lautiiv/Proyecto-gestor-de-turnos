from datetime import datetime, date
from dominio.turno import Turno

def menu_opcion_uno_turno(servicio):
    #Registra el turno
    print("1. Si usted sabe el id del paciente \n2. Si quiere ver los id de los pacientes.")
    try:
        opcion = int(input("\nSeleccione una opcion: "))
    except ValueError:
        print("Ingrese una opcion valida")
        return
    if opcion == 1:
        try:#input
            id_paciente = int(input("Ingrese el ID: "))
            print("En que resonador desea registrar el turno? \n1. Resonador 1.5#1\n2. Resonador 1.5#2\n3. Resonador 3T")
            id_resonador = int(input("Ingrese el resonador que desea: "))
            fecha_str = input("Fecha (YYYY-MM-DD): ")
            print("IMPORTANTE: Los turnos se registran CADA 30 MINUTOS")
            print("Horarios permitidos: :00 o :30 (Ejemplos: 09:00, 09:30, 10:00, etc.)")
            print("Los turnos solo pueden ser entre las 08:00 y 20:00hs")
            hora_str = input("Hora (HH:MM): ")
            nombre_estudio = input("Ingrese el nombre del estudio: ")
            #conversiones
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
            hora = datetime.strptime(hora_str, "%H:%M").time()
            fecha_hora = datetime.combine(fecha, hora)
        except ValueError:
            print("Ingrese datos validos")
            return            
            
        try:
            registrar_turno = Turno(None,id_paciente,id_resonador,fecha_hora,nombre_estudio,"activo")
            servicio.registrar_turno(registrar_turno)
        except ValueError as err:
            print(f'Error : {err}')   
    elif opcion == 2:
        servicio.listar_pacientes()


def menu_opcion_ver_turno(servicio):
    while True:
        print("\n== ¿Por que ID desea buscar? ==\n")
        print("1. Buscar turno por ID del turno\n2. Buscar turno por id del paciente\n0. Salir\n")
        try:
            menu = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Ingrese una opcion valida")
            
        if menu == 1:
            opcion_buscar_turno_por_id_turno(servicio)
   
        elif menu == 2:
            opcion_buscar_turno_por_id_paciente(servicio)
            
        elif menu == 0:
            break
            
        else:
            print("Ingrese una opcion valida")
            

def opcion_buscar_turno_por_id_turno(servicio):
    while True:
        print("\n== SUB MENU BUSCAR POR TURNO ID_TURNO ==\n")   
        print("\n1. Para ingresar el ID del turno\n2. Mostrar ID de los turnos\n0. Salir")
        try:
            sub_menu_buscar_turno_id = int(input("\nIngrese una opcion: "))
        except ValueError:
            print("Debe ingresar un numero")
            continue
        
        if sub_menu_buscar_turno_id == 1:
            try:
                id_input = int(input("Ingrese el ID del turno: "))
                servicio.informacion_turno_por_id_turno(id_input)
            except ValueError as err:
                print(err)
            break
        
        elif sub_menu_buscar_turno_id == 2:
            servicio.listar_id_turnos_pacientes()
            
        elif sub_menu_buscar_turno_id == 0:
            break
        
        else:
            print("Ingrese una opcion valida")
            
def opcion_buscar_turno_por_id_paciente(servicio):
    
    # Muestra los turnos del paciente a traves de su ID_PACIENTE
    # En caso de que no sepas el ID del paciente te muestra ID_PACIENTE acompañado de su nombre
    
    while True:
        print("\n== SUB MENU BUSCAR POR TURNO ID_PACIENTE ==\n")        
        print("1. Para ingresar el ID del paciente\n2. Mostrar lista de pacientes\n0. Salir")
        try:
            input_sub_menu_paciente = int(input("\nIngrese una opcion: "))
        except ValueError:
            print("Ingrese una opcion valida.\n")
            continue
        if input_sub_menu_paciente == 1:
            try:
                id_paciente_input = int(input("Ingrese el ID del paciente: "))
                servicio.informacion_turno_por_id_paciente(id_paciente_input)
            except ValueError as err:
                print(err)
                
        elif input_sub_menu_paciente == 2:        
            print("\nLISTA DE PACIENTES: \n")
            servicio.listar_pacientes()
                        
        elif input_sub_menu_paciente == 0:
            break
        else:
            print("Ingrese una opcion valida")
                     
def modificar_turno(servicio):

    #Incluye cancelar turno, reprogramar, cambiar equipo. Lo hace a traves de id_turno
    while True:
          
        id_ingresado = ingresar_turno_y_validar(servicio)
        print("\n== Modificar turno ==\n")

        turno = servicio.instanciar_turno_por_id(id_ingresado)
        print(f'Usted ingreso el ID_TURNO: {turno.id_turno}')
        
        print("\n1. Cancelar turno\n2. Reprogramar turno\n3. Cambiar equipo\n")
        try:
            menu_principal = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Ingrese una opcion correcta (0-1-2-3)")
            continue
        
        if menu_principal == 1:
            cancelar_turno(servicio,turno)
            break
        
        elif menu_principal == 2:
            pass
        
        elif menu_principal == 3:
            pass
        
        elif menu_principal == 0:
            break
        
        else:
            print("Ingrese una opcion valida")
            
def ingresar_turno_y_validar(servicio):
    #Cumple la primera parte de la funcion modificar turno. Solicita ID y/o muestra ID_TURNOS activos.
    
    while True:
        print("\n== Modificar turno ==\n")
        print("1. Para ingresar el ID del turno\n2. Mostrar lista de turnos activos\n0. Salir\n")
        try:
            opcion = int(input("Ingrese una opcion:"))            
        except ValueError:
            print("Ingrese una opcion valida")
            continue
            
        if opcion == 1:
            try:
                id_turno_a_modificar = int(input("Ingrese el ID del turno que quiere modificar: "))
            except ValueError:
                print("El id debe ser un numero")
                continue
            return id_turno_a_modificar
        elif opcion == 2:
            print("\n== TURNOS ACTIVOS ==\n") 
            turnos_activos = servicio.mostrar_id_turnos_activos()
            for turno in turnos_activos:
                print(turno)
            print("\n")
                
        elif opcion == 0:
            break
        
        else:
            print("Ingrese una opcion valida")
        
def cancelar_turno(servicio,turno : Turno):
    #Recibe un turno, se utiliza su id, se cancela el turno.
    while True:
        try:
            print("== Esta seguro que desea cancelar el turno? ==\n1. Si\n2. No")
            confirmacion = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Ingrese una opcion correcta")
            continue
    
        if confirmacion == 1:
            turno_cancelado = "cancelado"
            servicio.modificar_estado_turno(turno,turno_cancelado)
            break
    
        elif confirmacion == 2:
            break
    
def reprogramar_turno(servicio,id_turno):
    pass

def cambiar_equipo(servicio,id_turno):
    pass ##ESTA PUEDE QUEDAR PARA DESPUES
    
    
def ver_turnos_por_dia(servicio):
   #Funcion que mostrara los turnos de los 3 equipos en el dia de la fecha seleccionada. 
    while True:
        
        print("\n== Turnos ==\n")
    
        print("\n1. Ver los turnos de la fecha actual\n2. Ingresar fecha manualmente\n0. Salir\n")
        try:
            opcion_turnero = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Ingrese una opcion correcta (0-1-2)")
            continue
        
        if opcion_turnero == 1:
            hoy = date.today()
            turnos = servicio.ver_turnos_por_dia(hoy)
            
            if not turnos:
                print(F"No hay turnos el dia de la fecha {hoy}")
            else:
                print(f"==TURNOS DE LA FECHA {hoy}")
                for turno in turnos:
                    fecha_turno,estudio, nombre, apellido, equipo = turno
                    print(fecha_turno,estudio,nombre,apellido,f'equipo: {equipo}')
            

        elif opcion_turnero == 2:
            #funcion que desarrolle esta opcion, donde se llama al servicio.
            ver_turnero_por_fecha(servicio)
        
        elif opcion_turnero == 0:
            break
        
        else:
            print("Ingrese una opcion valida")


def ver_turnero_por_fecha(servicio):
    while True:
        
        fecha_input = input("Fecha (YYYY-MM-DD): ")
        
        try:
            fecha = datetime.strptime(fecha_input,"%Y-%m-%d").date()
        except ValueError:
            print("Ingrese el formato correcto de la fecha")
            continue
        
        turnos = servicio.ver_turnos_por_dia(fecha)
        
        if turnos:
            print(f"==TURNOS DE LA FECHA {fecha}")
            for turno in turnos:
                fecha_turno,estudio, nombre, apellido, equipo = turno
                print(fecha_turno,estudio,nombre,apellido,f'equipo: {equipo}')
            return
        
        else:
            print(F'== NO HAY TURNOS EL DIA DE LA FECHA {fecha} ==')
            return

        