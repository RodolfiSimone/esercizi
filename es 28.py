'''Dato un elenco di studenti partecipanti a una gara sportiva di lancio del peso visualizza il valore del lancio del vincitore'''

nomi = input("Nomi di ogni partencipante separati da uno spazio: ").split()
punteggi = []
for i in range(len(nomi)):
    punteggio = int(input("Il punteggio del partencipante corrispondente: "))
    punteggi.append(punteggio)

punteggio_max = max(punteggi)
indice = int(punteggi.index(punteggio_max))
vincitore = nomi[indice]
print("Il vincitore è : ", vincitore,"con", punteggio_max, "punti")