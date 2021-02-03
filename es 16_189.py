'''date le nazioni e le rispettive capitali, permettere di visualizzare le capitali partendo dalla nazione'''

def nazione_capitale(diz_naz_cap):
    nazione = input("Inserire la nazione di cui si vuole sapere la capitale ")
    if nazione in diz_naz_cap:
        print("La capitale de", nazione,"è : ",  diz_naz_cap[nazione])
    else:
        print("La capitale della nazione cercata non è stata inserita")


def main():
    diz_naz_cap = dict()
    while True:
        naz_cap = input("inserire il nome della nazione e la capitale separate da una virgola ").split(", ")
        diz_naz_cap[naz_cap[0]] = naz_cap[1]            
        controllo = input("scrivere 'si', se si vogliono inserire altre nazioni, altrimenti scrivere 'no' ")
        if controllo == "no":
            break
    
    nazione_capitale(diz_naz_cap)


main()
