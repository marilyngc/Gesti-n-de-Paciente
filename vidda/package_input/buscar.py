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
       
