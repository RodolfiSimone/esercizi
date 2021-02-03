''' 
    partendo dall'esercizio 15_189 invertire la chiave ed il valore nel dizionario
    e permettere di visualizzare la nazione partendo dalla capitale
'''

def nazione_capitale(diz_naz_cap):
    nazione = input("Inserire la nazione di cui si vuole sapere la capitale ")
    if nazione in diz_naz_cap:
        print("La capitale de", nazione,"è :",  diz_naz_cap[nazione])
    else:
        print("La capitale della nazione cercata non è stata inserita")


def capitale_nazione(diz_naz_cap):
    diz_cap_naz = dict()
    for chiave in diz_naz_cap:
        diz_cap_naz[diz_naz_cap[chiave]] = chiave

    capitale = input("Inserire la capitale di cui si vuole sapere la nazione ")
    if capitale in diz_cap_naz:
        print("La nazione di", capitale,"è :",  diz_cap_naz[capitale])
    else:
        print("La nazione della capitale cercata non è stata inserita")

def main():
    diz_naz_cap = dict()
    while True:
        naz_cap = input("inserire il nome della nazione e la capitale separate da una virgola ").split(", ")
        if len(naz_cap) == 2:
            diz_naz_cap[naz_cap[0]] = naz_cap[1]            
        controllo = input("scrivere 'si', se si vogliono inserire altre nazioni, altrimenti scrivere 'no' ")
        if controllo == "no":
            break
    
    controllo = int(input("scrivere 1, se si vuole cercare tramite capitale, 2 se tramite nazione "))
    if controllo == 1:
        capitale_nazione(diz_naz_cap)
    else:
        nazione_capitale(diz_naz_cap)


main()
