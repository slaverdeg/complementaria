import matplotlib.pyplot as plt
import expansiontermicamineral as etm
import mineral as mi

def coeficiente_y_graficas (clase, a1, a2):

    m1 = etm.ExpansionTermicaMineral(clase, a1).expansion_termica()
    m2 = etm.ExpansionTermicaMineral(clase, a2).expansion_termica()

    def texto(m1,m2):
        return m1[0] + m1[2] + "\n\n" + m2[0] + m2[2]
    
    print(texto(m1,m2))
    plt.show()

coeficiente_y_graficas(mi.mineral, './graphite_mceligot_2016.csv', './olivine_angel_2017.csv')
