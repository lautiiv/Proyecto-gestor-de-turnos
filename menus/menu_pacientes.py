# OPCION CREAR PACIENTE

def opcion_uno_menu_pacientes(instancia_servicio_paciente):
     while True: 
                
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = int(input("Edad: "))
        obra_social = input("Obra social: ")
        telefono = input("ingrese su numero de telefono: ")
                
        try:
                        
            instancia_servicio_paciente.registrar_paciente(nombre,apellido,edad,obra_social,telefono)
                    
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
                        

# OPCION ELIMINAR PACIENTE

def opcion_tres_menu_pacientes(instancia_servicios): 
    while True:
        try:
            opcion_para_eliminar = int(input("\n1. Si sabe el ID del paciente a eliminar\n2. Mostrar el ID de todos los pacientes\n3. Salir\n"))
                        
            if opcion_para_eliminar == 1:
                try:
                    id_a_eliminar = int(input("Ingrese el ID: "))
                    instancia_servicios.eliminar_paciente(id_a_eliminar)
                except ValueError:
                    print("ERROR: Ingrese un dato valido")
                
                
            elif opcion_para_eliminar == 2:
                print("\nLISTA DE PACIENTES: \n")
                instancia_servicios.mostrar_pacientes()
                            
            elif opcion_para_eliminar == 3:
                break
            else:
                print("Ingrese una opcion valida. Debe ingresar un numero (1-2-3) ")
        except ValueError:
            print("Dato no valido, debe ser un numero")
                
#OPCION MOSTRAR PACIENTE

def opcion_cuatro_menu_pacientes(instancia_servicios):
    while True:
        try:
            
