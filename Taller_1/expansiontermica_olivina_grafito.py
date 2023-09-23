import matplotlib.pyplot as plt
import expansiontermicamineral as etm
import mineral as mi
from matplotlib.backends.backend_pdf import PdfPages

def coeficiente_y_graficas (clase, a1, a2):

    m1 = etm.ExpansionTermicaMineral(clase, a1)
    e1 = m1.expansion_termica()
    m2 = etm.ExpansionTermicaMineral(clase, a2)
    e2 = m2.expansion_termica()

    def texto(e1,e2):
        return e1[0] + e1[2] + "\n\n" + e2[0] + e2[2]
    
    print(texto(e1,e2))
    #plt.show()
    fig_1 = m1.fig
    fig_2 = m2.fig

    pp = PdfPages('Gráficas expansión térmica de olivina y grafito.pdf')
    fig_1.savefig(pp, format='pdf')
    fig_2.savefig(pp, format='pdf')
    pp.close()

coeficiente_y_graficas(mi.mineral,'graphite_mceligot_2016.csv','olivine_angel_2017.csv')
