'''date le nazioni e le rispettive capitali, permettere di visualizzare le capitali partendo dalla nazione, usando due liste'''

def nazione_capitale(nazioni, capitali):
    nazione = input("Inserire la nazione di cui si vuole sapere la capitale ")
    if nazione in nazioni:
        print("La capitale de", nazione,"è : ",  capitali[nazioni.index(nazione)])
    else:
        print("La capitale della nazione cercata non è stata inserita")


def main():
    nazioni = []
    capitali = []
    while True:
        nazioni.append(input("inserire il nome della nazione "))
        capitali.append(input("inserire la capitale della nazione "))
        controllo = input("scrivere 'si', se si vogliono inserire altre nazioni, altrimenti scrivere 'no' ")
        if controllo == "no":
            break
    
    nazione_capitale(nazioni, capitali)


main()
