from .pacientes import opciones

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
        opcion = opciones("1.Promedio de las edades\n2.Promedio de las alturas\n3.Promedio de los pesos\n4.salir\n elija una opcion:")
        
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
       
                    