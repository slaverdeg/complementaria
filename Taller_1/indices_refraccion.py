import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def func_archivoyml_tuplas(ruta_yml: str) -> list:
  
    f = open(ruta_yml)
    texto_archivo = f.read()
    f.close()

    lista_unprocessed = texto_archivo.split('data: |\n')[1].split('\nSPECS')[0].split('  - type')[0].strip().split('\n        ')
    lista_final = []

    for k in lista_unprocessed:
        texto = k.split(' ')
        texto[0] = float(texto[0])
        texto[1] = float(texto[1])
        lista_final.append(tuple(texto))

    return lista_final



tuplaKapton=func_archivoyml_tuplas("C:/Users/laura/OneDrive/Escritorio/FISI2526-MetCompCompl-202320/Taller_1/Plásticos Comerciales/Kapton")

def grafica(tupla): 
    X=[]
    Y=[]
    for i in tupla:
        X.append(i[0])
        Y.append(i[1])

    X1=np.array(X)
    Y1=np.array(Y)

    plt.plot(X1,Y1)
    plt.show()


archivo=pd.read_csv("indices_refraccion.csv")

def ruta_yml(archivo):
    ga=archivo["Fabricante"]
    material=archivo["Material"]
    carpeta= archivo["Categoría"]
    ruta_yml= "C:/Users/laura/OneDrive/Escritorio/FISI2526-MetCompCompl-202320/Taller_1/"+carpeta +"/{}"
    ruta_yml2=ruta_yml.format(material)
    return ruta_yml2

def guardar_grafica(archivo:pd.DataFrame):
    for i in range(100):
        carpeta= archivo["Categoría"]
        material=archivo["Material"]
        ga=archivo.iloc[i]
        ruta=ruta_yml(ga)
        print(ruta)
        tupla=func_archivoyml_tuplas(ruta)
        rutassss="C:/Users/laura/OneDrive/Escritorio/FISI2526-MetCompCompl-202320/Taller_1/"+carpeta + "/{}" + ".PNG"
        rutassss2=ruta.format(material)
        X=[]
        Y=[]
        for j in tupla:
            X.append(j[0])
            Y.append(j[1])

        X1=np.array(X)
        Y1=np.array(Y)
        plt.clf()
        plt.plot(X1,Y1)
        
        plt.savefig(rutassss2)
        
        X.clear()
        Y.clear()

guardar_grafica(archivo)
