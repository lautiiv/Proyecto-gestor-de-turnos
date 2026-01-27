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
            while True:
                print("\n1. Para ingresar el ID del turno\n2. Mostrar lista de pacientes\n0. Salir")
                try:
                    input_id_turno = int(input("\nIngrese una opcion: "))
                except ValueError:
                    print("Ingrese un numero entero")
                if input_id_turno == 1:
                    try:
                        id_del_turno = int(input("\nIngrese el ID del turno: "))
                    except ValueError:
                        print("Ingrese un numero entero")
                    #METODO_PARA_DEVOLVER_INFORMACION_DEL_ID_TURNO
                elif input_id_turno == 2:
                    #METODO PARA MOSTRAR ID_TURNOS
                    pass
                    
                elif input_id_turno == 0:
                    break

            
        elif menu == 2:
            while True:
                
                print("\n1. Para ingresar el ID del paciente\n2. Mostrar lista de pacientes\n0. Salir")
                try:
                    input_id_paciente = int(input("\nIngrese una opcion: "))
                except ValueError:
                    print("Ingrese una opcion valida.\n")
                
                if input_id_paciente == 1:
                    pass
                    #metodo para mostrar los turnos
                
                elif input_id_paciente == 2:
                    
                    print("\nLISTA DE PACIENTES: \n")
                    servicio.listar_pacientes()
                        
                elif input_id_paciente == 0:
                    break
                else:
                    print("Ingrese una opcion valida")
            
        elif menu == 0:
            break
            
        else:
            print("Ingrese una opcion valida")