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
    return datos

def valida_proyectos_activos(proyectos:list[dict]):
    pass
convierte_csv_dict('Proyectos.csv')