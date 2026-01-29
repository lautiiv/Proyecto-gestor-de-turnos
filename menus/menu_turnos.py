from datetime import datetime
from dominio.turno import Turno

def menu_opcion_uno_turno(servicio):
    #id_turno,id_paciente,id_resonador,fecha,estudio
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
            registrar_turno = Turno(None,id_paciente,id_resonador,fecha_hora,nombre_estudio)
            servicio.registrar_turno(registrar_turno)
        except ValueError as err:
            print(f'Error : {err}')   
    elif opcion == 2:
        servicio.listar_pacientes()


def menu_opcion_ver_turno(servicio):
    while True:
        print("\n== SUBMENU VER TURNO ==\n")
        print("1. Buscar turno por ID del turno\n2. Buscar turno por id del paciente\n0. Salir\n")
        try:
            menu = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Ingrese una opcion valida")
            
        if menu == 1:
            opcion_buscar_turno_por_id(servicio)
   
        elif menu == 2:
            opcion_buscar_turno_por_id_paciente(servicio)
            
        elif menu == 0:
            break
            
        else:
            print("Ingrese una opcion valida")
            

def opcion_buscar_turno_por_id(servicio):
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
                servicio.informacion_turno(id_input)
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