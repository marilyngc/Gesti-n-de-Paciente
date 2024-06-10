from .reportes import mostrar_pacientes
from .pacientes import opciones

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
    """ Menu que salicita la clave para ordenar de forma descendiente o ascendiente

    Args:
        diccionario (dict): recibe el diccionario de todos los empleados
        
    Examples:
        # Ejemplo de uso:
        menu_ordenar_empleados(diccionario_empleados)
    """
    bandera_seguir = True
    ultima_lista = []
    while bandera_seguir:
        opcion = opciones("1. ordenar por nombre ascendiente\n2. ordenar por nombre descendiente\n3. ordenar por apellido ascendiente \n4. ordenar por apellido descendiente\n5. ordenar por altura ascendiente\n6. ordenar por altura descendiente\n7. ordenar por grupo sanguineo ascendiente\n8. ordenar por grupo sanguineo descendiente\n9.salir\n elija una opcion:")
        
        match opcion:
            case 1:
                ultima_lista = ordenar_ascendiente(diccionario, "nombre")
                mostrar_pacientes(ultima_lista)
            case 2:
                ultima_lista = ordenar_descendiente(diccionario, "nombre")
                mostrar_pacientes(ultima_lista)
            case 3:
                ultima_lista = ordenar_ascendiente(diccionario, "apellido")
                mostrar_pacientes(ultima_lista)
            case 4:
                ultima_lista = ordenar_descendiente(diccionario,"apellido")
                mostrar_pacientes(ultima_lista)
            case 5:
                ultima_lista = ordenar_ascendiente(diccionario,"altura")
                mostrar_pacientes(ultima_lista)
            case 6:
                ultima_lista = ordenar_descendiente(diccionario,"altura")
                mostrar_pacientes(ultima_lista)
            case 7:
                ultima_lista = ordenar_ascendiente(diccionario,"grupo sanguineo")
                mostrar_pacientes(ultima_lista)
            case 8:
                ultima_lista = ordenar_descendiente(diccionario,"grupo sanguineo")
                mostrar_pacientes(ultima_lista)

            case 9:
                seguir = input("seguro que quieres salir?")
                if seguir == "si":
                    print("Cambios guardados con exito")
                    bandera_seguir = False        
                else:
                    bandera_seguir = True  
            case _:
  
                print("ERROR: elija una opcion")
                
    return ultima_lista
