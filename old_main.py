from dao.paciente_dao import PacienteDAO
from dominio.paciente import Paciente
from db.db_conn import DBConn
from servicio.servicio_paciente import Servicios_Pacientes
#paciente_prueba = Paciente("Candela","Pellegrino",27,'MET',"2954446270")

db = DBConn(config_file="./config.ini")
dao = PacienteDAO(db)

instancia_servicio_pacientes = Servicios_Pacientes(db)


def main_menu():
    try:
        while True:
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
                
                while True: 
                
                    nombre = input("Nombre: ")
                    apellido = input("Apellido: ")
                    edad = int(input("Edad: "))
                    obra_social = input("Obra social: ")
                    telefono = input("ingrese su numero de telefono: ")
                
                    try:
                        
                        instancia_servicio_pacientes.registrar_paciente(nombre,apellido,edad,obra_social,telefono)
                    
                        print("Paciente creado correctamente.")
                    except Exception as e:
                        print("Error:", e)
                        break
                    
                    try: 
                        ingresar_mas_pacientes = int(input("Desea registrar un nuevo paciente? (1 = SI, 2 = NO): "))
                        
                        if ingresar_mas_pacientes == 1:
                            pass
                        elif ingresar_mas_pacientes == 2:
                            break
                        else:
                            print("Ingrese una opcion valida. Debe ingresar un numero (0-2)")
                    except ValueError:
                        print("Ingrese una opcion valida. Debe ingresar un numero (0-2)")
            
            elif opcion == 2:
                pass
            
            elif opcion == 3:
                while True:
                    try:
                        opcion_menu_tres = int(input("1. Eliminar paciente\n2. Regresar al menu pacientes\n"))
                        if opcion_menu_tres == 1:
                            while True:
                                try:
                                    opcion_para_eliminar = int(input("1. Ingrese ID del paciente a eliminar\n2. Mostrar el ID de todos los pacientes\n3. Salir\n"))
                                    if opcion_para_eliminar == 1:
                                        pass ## ACA SE ELIMINA EL PACIENTE 
                                    
                                    ELIF opcion_para_eliminar == 2:
                                    
                        elif opcion_menu_tres == 2:
                            break
                        else:
                            print("Ingrese una opcion valida. Debe ingresar un numero (1-2) ")
                    except ValueError:
                        print("Dato no valido, debe ser un numero")
                        
            
            elif opcion == 4:
                
                pass
            
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
            print('1. Asignar Turno\n2. Modificar turno\n3. Eliminar turno\n4. Ver turno\n5. Ver todos los turnos\n0. Salir')
            
            opcion = int(input("\nSeleccione una opcion: "))
            
            if opcion == 1:
                pass
            
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
                print("Ingrese una opcion valida. (0-5)")
                
        except ValueError:
            print("Ingrese una opcion valida. (0-5)")    
            
            
main_menu()
          
