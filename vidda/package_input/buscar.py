from inputs import get_int

def validar_paciente(dato:int,busqueda:str, diccionario:dict):
 
    for paciente in diccionario:
        if paciente[busqueda] == dato:
            return paciente
    return None  

def buscar_paciente(diccionario:dict, mensaje:str,clave:str):
    id_validado = get_int(f"Ingrese el {clave} del paciente a {mensaje}: ", 1,100000000, 3)
    paciente_encontrado = validar_paciente(id_validado,clave, diccionario)
    
    if paciente_encontrado:
        return paciente_encontrado
    else:
        f"ERROR: no se encontró el {clave} solicitado"  
       
