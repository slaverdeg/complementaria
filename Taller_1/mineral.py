import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class mineral:
    def __init__(self, nombre, dureza, lustre, rompimiento_por_fractura, color, composición, sistema_cristalino, specific_gravity):
        self.nombre = nombre
        self.dureza = dureza
        self.lustre = lustre
        self.rompimiento_por_fractura = rompimiento_por_fractura
        self.color = color
        self.composición = composición
        self.sistema_cristalino = sistema_cristalino
        self.specific_gravity = specific_gravity

    def es_silicato(self):
        if "Si" in str(self.composición) and "O" in str(self.composición):
            return True
        else:
            return False
        
    def densidad_SI(self):
        return float(self.specific_gravity)*1000
    
    def visualizar_color_mas_comun(self):
        fig, ax = plt.subplots(figsize=(2, 2))
        ax.set_facecolor(str(self.color))
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        return fig

    def imprimir_datos1 (self):
        d = str(self.dureza).stip()
        if self.rompimiento_por_fractura:
            t_r = "ROMPIMIENTO POR FRACTURA"
        else:
            t_r = "ROMPIMIENTO POR ESCISIÓN"
        s = str(self.sistema_cristalino).strip()
        return print(d+"\n"+t_r+"\n"+s)

