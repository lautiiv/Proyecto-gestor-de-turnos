
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
                        

def opcion_tres_menu_pacientes(instancia_servicios):
    while True:
        try:
            opcion_menu_tres = int(input("1. Eliminar paciente\n2. Regresar al menu pacientes\n"))
            if opcion_menu_tres == 1:
                while True:
                    try:
                        print("Si usted sabe el ID del paciente a eliminar ingrese la opcion 1. Si usted no sabe el ID ingrese la opcion 2")
                        opcion_para_eliminar = int(input("\n1. Ingrese ID del paciente a eliminar\n2. Mostrar el ID de todos los pacientes\n3. Salir\n"))
                        if opcion_para_eliminar == 1:
                            pass ## ACA SE ELIMINA EL PACIENTE 
                                    
                            #ELIF opcion_para_eliminar == 2:
                                    
                        elif opcion_para_eliminar == 2:
                            print("\nLISTA DE PACIENTES: \n")
                            instancia_servicios.mostrar_pacientes()
                            
                        elif opcion_para_eliminar == 3:
                            break
                        
                        else:
                            print("Ingrese una opcion valida. Debe ingresar un numero (1-2-3) ")
                    except ValueError:
                        print("Dato no valido, debe ser un numero")
                        
            elif opcion_menu_tres == 2:
                break
            else:
                print("Ingreso una opcion no valida. Las opciones deben ser 1 o 2")
        except ValueError:
            print("Dato no valido, debe ser un numero")