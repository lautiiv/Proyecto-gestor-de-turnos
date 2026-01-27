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
        servicio.mostrar_id_nombre_apellido_servicio()
