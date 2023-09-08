import numpy as np
import mineral as mi

archivo = open("minerales.txt", encoding="utf8")
lineas = archivo.readlines()
archivo.close()

MineralesL = []
for i in lineas[1:]:
    
    datos = i.strip().split('\t')

    nombre = datos[0]
    dureza = datos[1]
    rompimiento = datos[2]
    color = datos[3]
    composicion = datos[4]
    lustre = datos[5]
    s_gravity = datos[6]
    s_cristalino = datos[7]
    
    mineral_i = mi.mineral(nombre,dureza,lustre,rompimiento,color,composicion,s_cristalino,s_gravity)
    MineralesL.append(mineral_i)

Minerales = np.array(MineralesL)


def num_silicatos(m):
    s = 0
    for i in m:
        if i.es_silicato():
            s += 1
    return s

def densidad_promedio(m):
    n = 0
    d = 0
    for i in m:
        n += i.densidad_SI()
        d += 1
    p = n/d
    return round(p,2)
