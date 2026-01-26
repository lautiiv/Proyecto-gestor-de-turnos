from dao.paciente_dao import PacienteDAO
from dominio.paciente import Paciente
from db.db_conn import DBConn
from servicio.servicio_paciente import Servicios_Pacientes
from menus.menu_pacientes import opcion_uno_menu_pacientes, opcion_tres_menu_pacientes, opcion_cuatro_menu_pacientes, opcion_dos_menu_pacientes

from menus.menu_turnos import menu_opcion_uno_turno
from dao.turno_dao import TurnoDAO
from servicio.servicio_turno import Servicio_Turnos

db = DBConn(config_file="./config.ini")
dao = PacienteDAO(db)
dao_turno = TurnoDAO(db)

instancia_servicio_pacientes = Servicios_Pacientes(db)
servicio_turnos = Servicio_Turnos(db)


def main_menu():

    while True:
        try:
            print("\n===GESTOR DE TURNOS ===\n")
                    
            print("====OPCIONES===\n")
            print('1. menu pacientes \n2. menu turnos\n0. salir') 
                    
                    
            opcion = int(input("\nSeleccione una opcion: "))
                    
            if opcion == 1:
                    pacientes_menu()
                        
            elif opcion == 2:
                    turnos_menu()
                             
            elif opcion == 0:
                    print("Gracias por utilizar nuestro gestor de turnos")
                    return None         
            else:
                print("Ingrese una opcion valida (0-2)")
                        
        except ValueError:
            print("Ingrese una opcion valida. Debe ingresar un numero (0-2)")
            
            
            
            
def pacientes_menu():
    while True:
        try:
            print("\n== MENU PACIENTES ==\n")
            print('1. Crear paciente\n2. Modificar paciente\n3. Eliminar paciente\n4. Mostrar paciente\n5. Mostrar todos los pacientes\n0. Salir')
            
            opcion = int(input("\nSeleccione una opcion: "))
            
            if opcion == 1:
                opcion_uno_menu_pacientes(instancia_servicio_pacientes)
            
            elif opcion == 2:
                opcion_dos_menu_pacientes(instancia_servicio_pacientes)
                
            
            elif opcion == 3:
                opcion_tres_menu_pacientes(instancia_servicio_pacientes)
            
            elif opcion == 4:
                opcion_cuatro_menu_pacientes(instancia_servicio_pacientes)
            
            elif opcion == 5:
                print("\nLISTA DE PACIENTES: \n")
                instancia_servicio_pacientes.mostrar_pacientes()
            
            elif opcion == 0:
                break
            
            else:
                print("Ingrese una opcion valida")
            
        except ValueError:
            print("Debe ingresar un numero")
            
def turnos_menu():
    while True:
        try:
            print("\n== MENU TURNOS ==\n")            
            print('1. Registrar turno\n2. Reprogramar turno\n3. Cancelar turno\n4. Ver turno por ID\n5. Mostrar turnos del dia\n0. Salir')
        
            opcion = int(input("\nSeleccione una opcion: "))
        except ValueError:
            print("Debe ingresar un numero")
        if opcion == 1: 
            menu_opcion_uno_turno(servicio_turnos)
        
        elif opcion == 2:
            pass
        
        elif opcion == 3:
            pass
        
        elif opcion == 4:
            pass
        
        elif opcion == 5:
            pass
        
        elif opcion == 0:
            break
        else:
            print("Ingrese una opcion valida")


main_menu()