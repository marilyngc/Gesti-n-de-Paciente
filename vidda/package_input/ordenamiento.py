from reportes import mostrar_pacientes
from pacientes import opciones

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
        opcion = opciones("1. ordenar por nombre ascendiente\n2. ordenar por nombre descendiente\n3. ordenar por apellido ascendiente \n4. ordenar por apellido descendiente\n5. ordenar por altura ascendiente\n6. ordenar por altura descendiente\n7. ordenar por grupo sanguineo ascendiente\n8. ordenar por grupo sanguineo descendiente\n9.salir\n elija una opcion:")
        
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
