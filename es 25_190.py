'''
Da un dizionario che ha come chiave la matricola e valore il voto elenca, le matricole in ordine crescente di voto
e poi indica quali voti sono stati assegnati, contati solo una volta
'''

import random
import operator

matricola_voti = {}
voti_presenti = []

for n in range(30):
    matricola_voti[n] = random.randint(1, 10,)
matricola_voti = dict( sorted(matricola_voti.items(), key=operator.itemgetter(1)))
for e in matricola_voti:
    print("il voto della matricola", e, "è", matricola_voti[e])

for e in matricola_voti.values():
    if e not in voti_presenti:
        voti_presenti.append(e)
print("I voti assegnati sono :", voti_presenti)
