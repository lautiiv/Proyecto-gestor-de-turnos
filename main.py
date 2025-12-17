from dao.paciente_dao import PacienteDAO
from dominio.paciente import Paciente
from db.db_conn import DBConn

#paciente_prueba = Paciente("Candela","Pellegrino",27,'MET',"2954446270")

db = DBConn(config_file="./config.ini")
dao = PacienteDAO(db)


nombre = "Lautaro"
apellido = "Villafa"
edad  = 27
obra_social = "boreal"
telef = "2999999"

paciente_prueba2 = Paciente(nombre, apellido, edad, obra_social, telef)
#print(paciente_prueba2)
#dao.registrar_paciente(paciente_prueba2)
#dao.eliminar_paciente(3)
#print("eliminado con exito")

dao.mostrar_paciente_por_id(2)


print("Hola xd")

dao.mostrar_todos_pacientes()
'''
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
            print("Debe ingresar un numero")


def pacientes_menu():
    while True:
        try:
            print("\n== MENU PACIENTES ==\n")
            print('1. Crear paciente\n2. Modificar paciente\n3. Eliminar paciente\n4. Mostrar paciente\n5. Mostrar todos los pacientes\n0. Salir')
            
            opcion = int(input("\nSeleccione una opcion: "))
            
            if opcion == 1:
                nombre = input("Nombre: ").strip()
                apellido = input("Apellido: ").strip()
                edad = int(input("Edad: "))
                obra_social = input("Obra social: ").strip()
                telefono = input("ingrese su numero de telefono").strip()
                
                try:
                    #servicio_pacientes.crear_paciente(nombre,apellido,edad,obra_social,telefono) #utilizarla cuando exista el metodo.
                    print("Paciente creado correctamente.")
                except Exception as e:
                    print("Error:", e)
            
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
                print("Ingrese una opcion valida")
                
        except ValueError:
            print("Debe ingresar un numero")    
            
            
main_menu()
          

'''