from .inputs import *

contador_id = 1
empleados_maximos = 3

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
    
def buscar_paciente_id(diccionario:dict, mensaje:str):
    id_validado = get_int(f"Ingrese el ID del paciente a {mensaje}: ", 1, 20, 3)
    paciente_encontrado = validar_paciente(id_validado,"id", diccionario)
    
    if paciente_encontrado:
        return paciente_encontrado
    else:
        "ERROR: no se encontró el id solicitado"  

def buscar_paciente_dni(diccionario:dict,mensaje:str):
    dni_validado = get_int(f"Ingrese el DNI del paciente a {mensaje}: ", 1, 20, 3)
    paciente_encontrado = validar_paciente(dni_validado,"dni", diccionario)
    
    if paciente_encontrado:
        return paciente_encontrado
    else:
        "ERROR: no se encontró el DNI solicitado"  
            
            
            
def menu_modificar_empleado(id_paciente):
    bandera_seguir = True
    
    while bandera_seguir:
        opcion = int(input("1. Ingresar nombre a cambiar\n2. Ingrese apellido a cambiar\n3.La edad a cambiar\n4.Ingrese la altura a cambiar\n5.Ingrese el peso a cambiar:\n6. Ingrese el DNI a cambiar\n7.Ingrese el grupo sanguineoa cambiar\n8.salir\n elija una opcion:"))
        
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
 
def mostrar_paciente_dni():
    ### queda pendiente arreglar tema de DNI
    pass        
def mostrar_pacientes(diccionario:dict):

    if len(diccionario) > 0:
        print("*" * 110)
        print(f"| {"NOMBRE":<12} | {"APELLIDO":<12} | {"EDAD":<12} | {"ALTURA":<12} | {"PESO":<12} | {"DNI":<12} |{"GRUPO SANGUÍNEO":<12} |")
        print("_" * 110)
    
        for paciente in diccionario:
            nombre = paciente["nombre"] 
            apellido = paciente["apellido"] 
            edad = paciente["edad"] 
            altura = f"{paciente["altura"]}cm "  
            peso = f"{paciente["peso"]}KG "  
            dni = paciente["dni"]   
            grupo_sanguineo = paciente["grupo sanguineo"]   
            print(f"| {nombre:<12} | {apellido:<12} | {edad:<12} | {altura:<12} |{peso:<12} |{dni:<12} |{grupo_sanguineo:<12} |")

        print("*" * 110)    
    else:
        print("No hay pacientes registrados.....")
        
def ordenar_ascendiente(diccionario:dict,clave:str):
    for i in range(len(diccionario)):
        for j in range(i + 1, len(diccionario)):
            if diccionario[i][clave] > diccionario[j][clave]:
                diccionario[i], diccionario[j] =  diccionario[j], diccionario[i]
                
    return diccionario            
                
def ordenar_descendiente(diccionario:dict,clave:str):
    for i in range(len(diccionario)):
        for j in range(i + 1, len(diccionario)):
            if diccionario[i][clave] < diccionario[j][clave]:
                diccionario[i], diccionario[j] =  diccionario[j], diccionario[i]
    return diccionario            
           
def menu_ordenar_empleados(diccionario:dict):
    bandera_seguir = True
    
    while bandera_seguir:
        opcion = int(input("1. ordenar por nombre ascendiente\n2. ordenar por nombre descendiente\n3. ordenar por apellido ascendiente \n4. ordenar por apellido descendiente\n5. ordenar por altura ascendiente\n6. ordenar por altura descendiente\n7. ordenar por grupo sanguineo ascendiente\n8. ordenar por grupo sanguineo descendiente\n9.salir\n elija una opcion:"))
        
        match opcion:
            case 1:
                ordenar_nombres = ordenar_ascendiente(diccionario, "nombre")
                mostrar_pacientes(ordenar_nombres)
            case 2:
                ordenar_nombres = ordenar_descendiente(diccionario, "nombre")
                mostrar_pacientes(ordenar_nombres)
            case 3:
                ordenar_apellido = ordenar_ascendiente(diccionario, "apellido")
                mostrar_pacientes(ordenar_apellido)
            case 4:
                ordenar_apellido = ordenar_descendiente(diccionario,"apellido")
                mostrar_pacientes(ordenar_apellido)
            case 5:
                ordenar_altura = ordenar_ascendiente(diccionario,"altura")
                mostrar_pacientes(ordenar_altura)
            case 6:
                ordenar_altura = ordenar_descendiente(diccionario,"altura")
                mostrar_pacientes(ordenar_altura)
            case 7:
                ordenar_grupo_sanguineo = ordenar_ascendiente(diccionario,"grupo sanguineo")
                mostrar_pacientes(ordenar_grupo_sanguineo)
            case 8:
                ordenar_grupo_sanguineo = ordenar_descendiente(diccionario,"grupo sanguineo")
                mostrar_pacientes(ordenar_grupo_sanguineo)

            case 9:
                seguir = input("seguro que quieres salir?")
                if seguir == "si":
                    print("Cambios guardados con exito")
                    bandera_seguir = False        
                else:
                    bandera_seguir = True  
            case _:
                print("ERROR: elija una opcion")

def dni_paciente(diccionario:dict):
    dni = get_int("El DNI tiene que ser mayor a 4.000.000: ",4000000, 100000000, 3 )
    dni_validado = validar_paciente(dni,"dni", diccionario)
    
    if dni_validado:
        for clave,valor in dni_validado.items():
            print(f"{clave} --> {valor}")
    else:
        "ERROR: no se encontró el DNI solicitado"  
                    
def sacar_promedio(clave:str,diccionario:dict):
    suma = 0
    contador = 0
    for lista in diccionario:
        suma += lista[clave]
        contador += 1
    
    promedio = suma / contador
    return promedio 

def menu_promedio(diccionario:dict):
    bandera_seguir = True
    
    while bandera_seguir:
        opcion = int(input("1.Promedio de las edades\n2.Promedio de las alturas\n3.Promedio de los pesos\n4.salir\n elija una opcion:"))
        
        match opcion:
            case 1:
                promedio_edades = sacar_promedio("edad", diccionario)
                print(f"El promedio de las edades es: {promedio_edades}")
            case 2:
                promedio_altura = sacar_promedio("altura", diccionario)
                print(f"El promedio de las altura es: {promedio_altura}")
            case 3:
                promedio_peso = sacar_promedio("peso", diccionario)
                print(f"El promedio de las pesos es: {promedio_peso}")

            case 4:
                seguir = input("seguro que quieres salir?")
                if seguir == "si":
                    print("Cambios guardados con exito")
                    bandera_seguir = False        
                else:
                    bandera_seguir = True  
            case _:
                print("ERROR: elija una opcion")
       
                    