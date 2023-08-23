import matplotlib.pyplot as plt
from app import instance


def grafico_dia(id):
    
    dias = instance._getDataDay(id)

    dia1=0
    dia2=0
    dia3=0
    dia4=0
    dia5=0
    dia6=0
    dia7=0
        
        
    if(len(dias) >= 7):
        dia7 = dias[len(dias)-7][2]
    if(len(dias) >= 6):
        dia6 = dias[len(dias)-6][2]
    if(len(dias) >= 5):
        dia5 = dias[len(dias)-5][2]
    if(len(dias) >=4):
        dia4 = dias[len(dias)-4][2]
    if(len(dias) >=3):
        dia3 = dias[len(dias)-3][2]
    if(len(dias) >=2):
        dia2 = dias[len(dias)-2][2]
    if(len(dias) >=1):
        dia1 = dias[len(dias)-1][2]
        
        
    dias = ['7','6','5', '4', '3', '2', '1']
    quantidades = [dia7, dia6, dia5, dia4, dia3, dia2, dia1]
        
    fig, ax = plt.subplots(figsize=(7, 5))
    bar_container = ax.bar(dias, quantidades)
        
    ax.set(ylabel='Litros', xlabel='Dias Atrás')
    ax.set_title(('Quantidade em Litros nos últimos 7 dias'),fontsize=16)
    ax.bar_label(bar_container)
        
    plt.savefig("./static/graficos/grafico_leite.png", transparent=True)
        
        
def grafico_tempos(id):
    
    tempos = instance._getTemposLeite(id)
        
    quente = tempos[0]
    frio = tempos[1]
    mediano = tempos[2]
        
    labels = ['Quente', 'Frio', 'Mediano']
    vals = [quente, frio, mediano]
        
    fig, ax = plt.subplots(figsize=(7, 5))
        
    ax.pie(vals, labels=labels, autopct="%.2f%%")
    ax.set_title(('Quantidade de Leite Produzido em Relação ao Tempo/Clima'), fontsize=16)
        
    plt.savefig("./static/graficos/grafico_tempos.png", transparent= True)
        