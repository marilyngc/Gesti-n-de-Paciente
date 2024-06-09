from .buscar import buscar_paciente

def mostrar_paciente_formateado(paciente):
    """Imprime los datos de un paciente en formato tabular.

    Esta función toma un diccionario que contiene los datos de un paciente y los imprime
    en forma de fila tabulada.

    Args:
        paciente (dict): Diccionario que contiene los datos del paciente, incluyendo 'nombre',
            'apellido', 'edad', 'altura', 'peso', 'dni' y 'grupo sanguineo'.

    Examples:
        # Ejemplo de uso:
        paciente = {
            "nombre": "Juan",
            "apellido": "Pérez",
            "edad": 30,
            "altura": 175,
            "peso": 75.5,
            "dni": "12345678",
            "grupo sanguineo": "A+"
        }
        mostrar_paciente_formateado(paciente)
    """
    nombre = paciente["nombre"]
    apellido = paciente["apellido"]
    edad = paciente["edad"]
    altura = f"{paciente['altura']} cm"
    peso = f"{paciente['peso']} KG"
    dni = paciente["dni"]
    grupo_sanguineo = paciente["grupo sanguineo"]
    print(f"| {nombre:<12} | {apellido:<12} | {edad:<12} | {altura:<12} | {peso:<12} | {dni:<12} | {grupo_sanguineo:<12} |")

def mostrar_paciente_individual(diccionario, mensaje, clave):
    paciente = buscar_paciente(diccionario, mensaje, clave)
    
    if paciente:
        print("*" * 110)
        print(f"| {"NOMBRE":<12} | {"APELLIDO":<12} | {"EDAD":<12} | {"ALTURA":<12} | {"PESO":<12} | {"DNI":<12} |{"GRUPO SANGUÍNEO":<12} |")
        print("_" * 110)
        mostrar_paciente_formateado(paciente)
        print("*" * 110)
    else:
        print(f"ERROR: no se encontró el {clave} solicitado")

def mostrar_pacientes(diccionario: dict):
    """Muestra los pacientes almacenados en un diccionario de manera formateada.

    Esta función imprime en consola una tabla formateada con los datos de los pacientes almacenados
    en un diccionario, incluyendo su nombre, apellido, edad, altura, peso, DNI y grupo sanguíneo.

    Args:
        diccionario (dict): Diccionario que contiene los datos de los pacientes.


    Examples:
        # Ejemplo de uso:
        mostrar_pacientes(diccionario_pacientes)
    """
    if len(diccionario) > 0:
        print("*" * 110)
        print(f"| {"NOMBRE":<12} | {"APELLIDO":<12} | {"EDAD":<12} | {"ALTURA":<12} | {"PESO":<12} | {"DNI":<12} |{"GRUPO SANGUÍNEO":<12} |")
        print("_" * 110)
    
        for paciente in diccionario:
            mostrar_paciente_formateado(paciente)

        print("*" * 110)
    else:
        print("No hay empleados registrados.....")

