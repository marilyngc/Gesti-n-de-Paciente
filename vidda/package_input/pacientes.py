from .inputs import *

contador_id = 1
empleados_maximos = 3

def opciones(mensaje:str):
    opcion_valida = get_int(mensaje,1, 8, 5)
    
    return opcion_valida

def crear_paciente(id:int):

    nombre_validado = validar_caracteres("Ingrese su nombre: ")

    apellido_validado = validar_caracteres("Ingrese su apellido: ")
    
    edad_validado = get_int("Ingrese su edad: ", 1, 120, 3)
    
    altura_validado = get_int("Ingrese su altura: ", 30, 230, 3)

    peso_validado = get_float("Ingrese su peso: ", 10, 300, 3)
    
    dni_validado = get_int("El DNI tiene que ser mayor a 4.000.000: ",4000000, 100000000, 3 )
        
    grupo_sanguineo_validado = validar_grupo_sanguineo("Ingrese su tipo sanguineo: ")

    if None in[nombre_validado, apellido_validado,edad_validado,altura_validado,peso_validado,dni_validado,grupo_sanguineo_validado]:
         return None
        
    else:
        empleado_creado = {"id":id, 
                           "nombre":nombre_validado, 
                           "apellido":apellido_validado, 
                           "edad": edad_validado,
                           "altura": altura_validado,
                           "peso": peso_validado,
                           "dni":dni_validado,
                           "grupo sanguineo": grupo_sanguineo_validado
                           }

        return empleado_creado
    
def agregar_paciente(empleados):

    if len(empleados) < empleados_maximos + 1:
        global contador_id
        empleado_creado = crear_paciente(contador_id)
        
        empleados.append(empleado_creado)
        contador_id += 1
        return "Paciente dado de alta con exito"
    else:
        return "ERROR: no se puede agregar mas de 20 pacientes"   
    
    
            
def menu_modificar_paciente(id_paciente):
    bandera_seguir = True
    
    while bandera_seguir:
        opcion = opciones("1. Ingresar nombre a cambiar\n2. Ingrese apellido a cambiar\n3.La edad a cambiar\n4.Ingrese la altura a cambiar\n5.Ingrese el peso a cambiar:\n6. Ingrese el DNI a cambiar\n7.Ingrese el grupo sanguineoa cambiar\n8.salir\n elija una opcion:")
        
        match opcion:
            case 1:
                nombre_validado = validar_caracteres("Ingrese el nombre: ")
                
                id_paciente["nombre"] = nombre_validado    
                
            case 2:

                apellido_validado = validar_caracteres("Ingrese el apellido: ")

                id_paciente["apellido"] = apellido_validado
                
            case 3:
                edad_validado = get_int("Ingrese su edad: ", 1, 120, 3)

                id_paciente["edad"] = edad_validado
            case 4:

                altura_validado = get_int("Ingrese su altura: ", 30, 230, 3)
                
                id_paciente["altura"] = altura_validado
                
            case 5:
                peso_validado = get_float("Ingrese su peso: ", 10, 300, 3)

                id_paciente["peso"] = peso_validado          
            case 6:
                dni_validado = get_int("El DNI tiene que ser mayor a 4.000.000: ",4000000, 100000000, 3 )

                id_paciente["dni"] = dni_validado
            case 7:
                grupo_sanguineo_validado = validar_grupo_sanguineo("Ingrese su tipo sanguineo: ")

                id_paciente["grupo sanguineo"] = grupo_sanguineo_validado
            case 8:
                seguir = input("seguro que quieres salir?")
                if seguir == "si":
                    print("Cambios guardados con exito")
                    bandera_seguir = False        
                else:
                    bandera_seguir = True  
            case _:
                print("ERROR: elija una opcion")
                
def eliminar_paciente(clave:str, valor:int,diccionario:dict):
    for paciente in diccionario:
        if paciente[clave] == valor:
            diccionario.remove(paciente)
            return "Empleado eliminado de forma exitosa"



                    
