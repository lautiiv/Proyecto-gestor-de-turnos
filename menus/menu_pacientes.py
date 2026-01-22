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
                instancia_servicios.mostrar_id_nombre_apellido_servicio()
                            
            elif opcion_para_eliminar == 3:
                break
            else:
                print("Ingrese una opcion valida. Debe ingresar un numero (1-2-3) ")
        except ValueError:
            print("Dato no valido, debe ser un numero")
                
#OPCION MOSTRAR PACIENTE POR ID

def opcion_cuatro_menu_pacientes(instancia_servicios):
    while True:
        try:
            opcion_paciente_a_mostrar = int(input("\n1. Si sabe el ID del paciente a mostrar\n2. Mostrar el ID de todos los pacientes\n3. Salir\n"))
            
            if opcion_paciente_a_mostrar == 1:
                try:
                    id_a_mostrar = int(input("Ingrese el ID: "))
                    instancia_servicios.mostrar_paciente_por_id(id_a_mostrar)
                except ValueError:
                    print("ERROR: Ingrese un dato valido")
            
            elif opcion_paciente_a_mostrar == 2:
                instancia_servicios.mostrar_id_nombre_apellido_servicio()
                
            elif opcion_paciente_a_mostrar == 3:
                break
            else:
                print("Ingrese una opcion valida. Debe ingresar un numero (1-2-3) ")
        except ValueError:
            print("Dato no valido, debe ser un numero")         


#OPCION MODIFICAR PACIENTE POR ID

def opcion_dos_menu_pacientes(instancia_servicios):
    while True:
        try:
            input_menu = int(input("\n1. Si sabe el ID del paciente a modificar\n2. Mostrar el ID de todos los pacientes\n3. Salir\n"))
            
            if input_menu == 1:
                try:
                    id_paciente_a_modificar = int(input("Ingrese el ID: "))
                       
                    paciente = instancia_servicios.obtener_instancia_paciente_por_id(id_paciente_a_modificar)
                    
                    #Se muestran datos del paciente a modificar
                    print(f"Usted a seleccionado el paciente con ID: {id_paciente_a_modificar}\nA continuacion se le mostraron los datos: \n")
                    print(paciente)
                    
                    modificar_datos_pacientes(instancia_servicios,paciente)
                    
                    print("Desea modificar algun atributo atributo? \n")
                    
                except ValueError:
                    print("ERROR: Ingrese un dato valido")
            
            elif input_menu == 2: 
                instancia_servicios.mostrar_id_nombre_apellido_servicio()
            
            
            elif input_menu == 3:
                break
            else:
                print("Ingrese una opcion valida. Debe ingresar un numero (1-2-3) ")
                
        except ValueError:
            print("Dato no valido debe ser un numero")
            
def modificar_datos_pacientes(servicio,paciente_a_modificar):
    while True:
        try:
            print("Que atributo desea modificar?")
            print("\n1. Nombre\n2. Apellido\n3. Edad\n4. Obra_social\n5. Telefono\n6. Salir y actualizar")
            
            menu = int(input())
            
            if menu == 1:
                try:
                    nombre = input("Introduzca el nuevo nombre: ").strip()
                    paciente_a_modificar.nombre = nombre
                    print("Nombre actualizado con exito\n")
                    
                except ValueError:("Error, introduzca un dato valido")    
            
            elif menu == 2:
                try:
                    apellido = input("Introduzca el nuevo apellido: ").strip()
                    paciente_a_modificar.apellido = apellido
                    print("Apellido actualizado con exito\n")
                except ValueError:("Error, introduzca un dato valido")    
            
            elif menu == 3:
                try:
                    edad = int(input("Introduzca la nueva edad: "))
                    paciente_a_modificar.edad = edad
                    print("Edad actualizada con exito\n")
                except ValueError:("Error, introduzca un dato valido")
            
            elif menu == 4:
                try:
                    obra_social = input("Introduzca su nueva obra social: ").strip()
                    paciente_a_modificar.obra_social = obra_social
                    print("Obra social actualizada con exito\n")
                except ValueError:("Error, introduzca un dato valido")
                
            
            elif menu == 5:
                try:
                    telefono = input("Introduzca su nuevo telefono: ").strip()
                    paciente_a_modificar.telefono = telefono
                    print("Telofono actualizado con exito\n")
                except ValueError:("Error, introduzca un dato valido")
                    
            
            elif menu == 6:
                servicio.update_paciente(paciente_a_modificar)
                break
            
            else:
                print("Ingrese una opcion valida. Debe ingresar un numero (1-2-3-4-5-6)")
        except ValueError:
            print("Dato no valido debe ser un numero")