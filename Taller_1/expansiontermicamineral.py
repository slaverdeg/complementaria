import numpy as np
import mineral as mi
import matplotlib.pyplot as plt
from os import path

class ExpansionTermicaMineral:
    def __init__(self, Mineral, archivo):

        a = open(archivo)
        self.nombre_archivo = path.basename(archivo)
        lineas = a.readlines()
        a.close()
        T = []
        V = []

        for k in lineas[1:]:
            T.append(float(k.strip().split(',')[0]))
            V.append(float(k.strip().split(',')[1]))

        self.T = T
        self.V = V
        
    def expansion_termica(self):

        if "graphite" in self.nombre_archivo:
            n = "Grafito"
            
        elif "olivine" in self.nombre_archivo:
            n = "Olivino"
            
        else:
            n = "mineral analizado"

        d = []

        for i in range(1,(len(self.T)-1)):

            de = (self.V[i+1] - self.V[i-1]) / (abs(self.T[i]-self.T[i-1]) + abs(self.T[i+1]-self.T[i]))
            d.append(de)
            
        alpha = []
        
        for i in range(1,len(self.V)-1):
            a = (1/self.V[i]) * (d[i-1])
            alpha.append(a)
            
        arreglo_alpha = np.array(alpha) 
        error = np.std(arreglo_alpha)/np.sqrt(len(arreglo_alpha))
        
        fig,axs = plt.subplots(nrows=1,ncols=2,figsize=(18,4.5))
        plt.suptitle(n)
        
        axs[0].scatter(x=self.T,y=self.V)
        axs[0].set_ylabel(r'Volumen (cm³)')
        axs[0].set_xlabel('Temperatura (°C)')
        axs[0].set_title('Volumen vs Temperatura')
        
        axs[1].scatter(x=self.T[1:len(self.T)-1],y=alpha)
        axs[1].set_ylabel(r'Coeficiente de Expansión Térmica (°C⁽⁻¹⁾)')
        axs[1].set_xlabel('Temperatura (°C)')
        axs[1].set_title('Coeficiente de Expansión Térmica vs Temperatura')
        
        return ["\nEl Coeficiente de Expansión Térmica del " + n + " depende de la Temperatura del mmismo.\nPor ejemplo a " + str(self.T[1]) + "°C el Coeficiente de Expansión es igual a " + str(alpha[0]) +"°C⁽⁻¹⁾.\n" , "\nEl error global en el cálculo del Coeficiente de Expansión Térmica es " + str(error) + "."+"\n" , "\nLas gráficas corresponden a el Volumen y el Coeficiente de Expansión Térmica en función de la Temperatura respectivamente.\n"]                         
