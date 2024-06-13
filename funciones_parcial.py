from datetime import datetime
def convierte_csv_dict(path:str):
    '''
    Devuelve DATOS
    '''
    datos = []
    archivo = open(path,'r+')
    lineas = archivo.readlines()
    #Utilizamos el encabezado ya realizado en el csv para no hardcodear.
    #LINEA 0 = ENCABEZADO
    encabezados = lineas[0].strip().split(",")
    #por cada linea hago una iteracion MENOS la linea del encabezado
    for i in range(1,len(lineas)):
        valores = lineas[i].strip().split(",")
        proyecto = {}
        for i in range(len(encabezados)):
            proyecto[encabezados[i]] = valores[i]
        datos.append(proyecto)
    archivo.close()
    return datos

def valida_proyectos_activos(proyectos:list[dict]):
    '''
    Devuelve TRUE si se pasa de los 50 proyectos.
    '''

    cont = 0
    for i in range(len(proyectos)):
        if proyectos[i]["Estado"] == "Activo":
            cont += 1
        if cont > 50:
            #print("ALERTA! LIMITE DE PROYECTOS ALCANZADO \nElimine un proyecto activo para seguir agregando.")
            return True
    return False
#Verifica nombre del proyecto
def verifica_nombre_proyecto():
    while True:
        nombre = input("Ingrese nombre del proyecto:")
        if (len(nombre) < 30) and (nombre.isalpha()):
            return nombre

#Verif descripcion
def verifica_descripcion():
    while True:
        descripcion = input("Ingrese descripcion del proyecto: ")
        if (len(descripcion) < 200):
            return descripcion

def verifica_presupuesto():
    while True:
        presupuesto = input("Ingrese presupuesto del proyecto: ")
        if (presupuesto.isnumeric()):
            presupuesto = int(presupuesto)
            if presupuesto < 500000:
                return presupuesto


def ingreso_fecha_inicio_fin():
    '''
    Devuelve DOS VALORES OJO! primero fecha inicio, 
    despues fecha fin.
    '''
    while True:
        try:
            fecha_inicio = input("Ingrese fecha inicio FORMATO DD/MM/AAAA: ")
            fecha_inicio = datetime.strptime(fecha_inicio,'%d/%m/%Y')
            break
        except:
            print("FECHA INVALIDA")
    while True:
        try:
            fecha_fin = input("Ingrese fecha fin FORMATO DD/MM/AAAA: ")
            fecha_fin = datetime.strptime(fecha_fin,'%d/%m/%Y')
            if not(fecha_fin > fecha_inicio):
                print("FECHA INVALIDA")
                continue
            return str(fecha_inicio),str(fecha_fin)
        except:
            print("FECHA INVALIDA")
def agrega_proyecto(path:str):
    pass


def ingresa_proyecto(proyectos:list[dict]):
    nuevo_proyecto = {}
    nombre = verifica_nombre_proyecto()
    descripcion = verifica_descripcion()
    presupuesto = verifica_presupuesto()
    fecha_inicio,fecha_final = ingreso_fecha_inicio_fin()
    last_id = int(proyectos[-1]["id"])
    last_id += 1
    
    #SUBO DATOS AL NUEVO DICCIONARIO
    
    nuevo_proyecto["id"] = last_id  
    nuevo_proyecto["Nombre del Proyecto"] = nombre
    nuevo_proyecto["Descripcion"] = descripcion
    nuevo_proyecto["Fecha de inicio"] = fecha_inicio
    nuevo_proyecto["Fecha de Fin"] = fecha_final
    nuevo_proyecto["Presupuesto"] = presupuesto
    nuevo_proyecto["Estado"] = "Activo"
    
    return nuevo_proyecto


def imprimir_menu():
    print("1. Ingresar proyecto")
    print("2. Modificar proyecto")
    print("3. Cancelar proyecto")
    print("4. Comprobar proyectos")
    print("5. Mostrar todos")
    print("6. Calcular presupuesto promedio")
    print("7. Buscar proyecto por nombre")
    print("8. Ordenar proyectos")
    print("9. Retomar proyecto")
    print("12. Salir")


def opcion_menu_1():
    datos_dict = convierte_csv_dict('Proyectos.csv')
    if valida_proyectos_activos(datos_dict) == False:
        nuevo_proyecto = ingresa_proyecto(convierte_csv_dict('Proyectos.csv'))
        datos_dict.append(nuevo_proyecto)
    else:
        print('ERROR, PROYECTOS ACTIVOS SUPERAN LOS 50.')
        sigue = True
    continuar = input('Desea seguir ingresando? S/N: ')
    if continuar == "S":
        sigue = True
    elif continuar == "N":
        sigue = False
    else:
        sigue = False
    return sigue,datos_dict


def opcion_menu_2(datos_dict:list[dict]):

    id_busqueda = input("Ingrese la ID del proyecto: ")
    if id_busqueda.isnumeric():
        id_busqueda = int(id_busqueda)
    
    print("1- Modificar nombre: ")
    print("2- Modificar Descripcion: ")
    print("3- Modificar Fecha de inicio: ")
    print("4- Modificar Fecha de Fin: ")
    print("5- Modificar Presupuesto: ")
    print("6- Modificar Estado: ")
    opcion = input("Ingrese la opcion: ")
    datos_dict[]
    while True:
        match opcion:
            case "1":
                


def menu_ingresos(datos_dict:list[dict]):
    while True:
        imprimir_menu()
        opcion = input("Elija su opcion: ")
        match opcion:
            case "1":
                while True:
                    sigue,datos_dict = opcion_menu_1()
                    if sigue == True:
                        continue
                    else:
                        break
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                pass
            case "8":
                pass
            case "9":
                pass
            case "12":
                break
menu_ingresos()