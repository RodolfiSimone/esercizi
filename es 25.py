'''Si conscono i nomi dei partecipanti ed i punteggi, visualizzare l'elenco in ordine alfabetico e poi in ordine decrescente di punteggio'''

candidato_a = input("nome del primo candidato")
punteggio_a = int(input("punteggio del primo candidato"))
candidato_b = input("nome del secondo candidato")
punteggio_b = int(input("punteggio del secondo candidato"))
nomi = [candidato_a, candidato_b]
nomi.sort()
punteggi = [punteggio_a, punteggio_b]
punteggi.sort()
punteggi.reverse()
print(nomi, punteggi)