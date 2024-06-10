from .inputs import get_int

def validar_paciente(dato:int,busqueda:str, diccionario:dict):
 
    for paciente in diccionario:
        if paciente[busqueda] == dato:
            return paciente
    return None  

def buscar_paciente(diccionario:dict, mensaje:str,clave:str):
    """Busca un paciente en el diccionario según la clave proporcionada.

    Esta función busca un paciente en el diccionario según la clave especificada
    (como 'nombre', 'apellido', 'dni', etc.) y devuelve el diccionario del paciente
    si se encuentra, o None si no se encuentra.

    Args:
        diccionario (dict): Diccionario que contiene los datos de los pacientes.
        mensaje (str): Mensaje que indica la acción que se está realizando, como
            "buscar", "modificar", etc.
        clave (str): La clave del diccionario por la cual se va a buscar al paciente.

    Returns:
        dict or error: Un diccionario que representa al paciente encontrado, o error si no se encuentra.

    Example:
        # Ejemplo de uso:
        pacientes = [
            {"nombre": "Juan", "apellido": "Pérez", "edad": 30, "dni": "12345678", "grupo sanguineo": "A+"},
            {"nombre": "María", "apellido": "Gómez", "edad": 25, "dni": "33555987", "grupo sanguineo": "AB-"}
        ]
        buscar_paciente(pacientes, "buscar", "dni")
    """
    id_validado = get_int(f"Ingrese el {clave} del paciente a {mensaje}: ", 1,100000000, 3)
    paciente_encontrado = validar_paciente(id_validado,clave, diccionario)
    
    if paciente_encontrado:
        return paciente_encontrado
    else:
        f"ERROR: no se encontró el {clave} solicitado"  

def buscar_grupo_sanguineo_compatible(diccionario, clave):
    
    dato_valido = get_int("El DNI tiene que ser mayor a 4.000.000: ", 4000000, 99999999, 3)       
    paciente_encontrado = validar_paciente(dato_valido,clave, diccionario)
    
    if paciente_encontrado:
        grupo_sanguineo = paciente_encontrado["grupo sanguineo"]

        grupos_compatibles = set()

        match grupo_sanguineo:
            case "A+":
                grupos_compatibles.update(["A+", "AB+"])
            case "A-":
                grupos_compatibles.update(["A+", "A-", "AB+", "AB-"])
            case "B+":
                grupos_compatibles.update(["B+", "AB+"])
            case "B-":
                grupos_compatibles.update(["B+", "B-", "AB+", "AB-"])
            case "AB+":
                grupos_compatibles.update(["AB+"])
            case "AB-":
                grupos_compatibles.update(["AB+", "AB-"])
            case "O+":
                grupos_compatibles.update(["O+", "A+", "B+", "AB+"])
            case "O-":
                grupos_compatibles.update(["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"])
            case _:
                print("No hay coincidencias")

        return grupos_compatibles
    else:
        print("No se encontró el dato ingresado")
    
def determinar_compartibilidad(clave, diccionario):
    grupo = buscar_grupo_sanguineo_compatible(diccionario, clave)
    pacientes_con_compartibilidad = []
    for paciente in diccionario:
        for sanguineo in grupo:
            if paciente["grupo sanguineo"] == sanguineo:
                if len(pacientes_con_compartibilidad) < 3:
                    pacientes_con_compartibilidad.append(paciente)
                else:
                    break  
    
    return print(f"grupo compatible: {grupo}\npacientes que son compatibles para que te donen: {pacientes_con_compartibilidad}")
               
                
                
                

