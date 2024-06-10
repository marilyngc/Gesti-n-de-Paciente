import re
def leer_archivos(path:str, lista):
    try:
        with open(path, "r", encoding="utf-8") as archivo:
           
            for linea in archivo:
              
                registro = re.split(",|\n",linea)
                diccionario = {
                    "id": registro[0],
                    "nombre": registro[1],
                    "apellido": registro[2],
                    "edad": int(registro[3]),
                    "altura": int(registro[4]),
                    "peso": float(registro[5]),
                    "dni": int(registro[6]),
                    "grupo sanguineo": registro[7]
                }
               
               
                lista.append(diccionario)
        return lista
               
                
    except:
        return "A ocurrido un error al generar la lista en el archivo"  
    
def guardar_empleados(path:str, lista:list):
    try:
        with open(path, "w", encoding="utf-8") as archivo:
            for paciente in lista:
                linea = f"{paciente['id']},{paciente['nombre']},{paciente['apellido']},{int(paciente['edad'])},{int(paciente['altura'])},{float(paciente['peso'])},{int(paciente['dni'])},{paciente['grupo sanguineo']}\n"

                archivo.write(linea)
                
               
    except:
        return "A ocurrido un error al generar la lista en el archivo"     

def guardar_id(path:str, conjunto:set):
    with open(path, "r", encoding="utf-8") as archivo:
        # contador_lineas = 0
        for linea in archivo:
            # if contador_lineas == 0:
            #     contador_lineas += 1
            #     continue
                            
            registro = re.split(",|\n",linea)
            set = registro[0]
            # contador_lineas += 1
            conjunto.add(int(set))  
    
    return conjunto 
                