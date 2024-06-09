from os import system
from package_input.pacientes import opciones, agregar_paciente,menu_modificar_paciente, eliminar_paciente
from package_input.buscar import buscar_paciente
from package_input.reportes import mostrar_pacientes, mostrar_paciente_individual
from package_input.utilidades import menu_promedio
from package_input.ordenamiento import menu_ordenar_empleados

pacientes = []

def menu_empleados(diccionario:dict):
    try:
        bandera_Seguir = True
        pacientes_alta = False
        
        while bandera_Seguir:
            
            opcion = opciones("1. Ingresar paciente\n2. Modificar paciente\n3. Eliminar paciente.\n4. Mostrar todos\n 5. Ordenar pacientes\n6. Buscar paciente por DNI \n7. Calcular promedio\n8. salir\n elija una opcion:")
            
            if opcion in range(2,8) and pacientes_alta is False:
                print("ERROR: Tiene que ingresar un paciente primero")
                continue
                
            match opcion:
                case 1:
                    mensaje = agregar_paciente(diccionario)
                    print(mensaje)
                    pacientes_alta = True

                case 2:
                    
                    id_paciente = buscar_paciente(diccionario, "modificar","id")
                    modificacion = menu_modificar_paciente(id_paciente)

                case 3:

                    dni_paciente = buscar_paciente(diccionario, "eliminar","dni")
                    empleado_eliminado = eliminar_paciente("dni",dni_paciente, diccionario)
                    print(empleado_eliminado)

                case 4:
                    tabla_empleados = mostrar_pacientes(diccionario)

                case 5:
                    ordenamiento = menu_ordenar_empleados(diccionario)

                case 6:
                    empleado = mostrar_paciente_individual(diccionario, "mostrar","dni")

                case 7:
                    resultado_promedio = menu_promedio(diccionario)
                    print(resultado_promedio)

                case 8:
                    seguir = input("seguro que quieres salir?")
                    if seguir == "si":
                        bandera_Seguir = False        
                    else:
                        bandera_Seguir = True  
                case _:
                    print("ERROR: elija una opcion")
        
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
        exit()  # Sale del programa limpiamente            
                
menu_empleados(pacientes)
                
system("pause")
system("cls")               
