'''Partendo dalla lista dell'es 25_190.py elenca la matricola degli studenti con una votazione superiore alla media generale'''

import random

matricola_voti = {}
matricola_voto_maggiore_media = []

for n in range(30):
    matricola_voti[n] = random.randint(1, 10,)

media_totale = sum(matricola_voti.values())/30
for e in matricola_voti:
    if matricola_voti[e] > media_totale :
        matricola_voto_maggiore_media.append(e)

print("La matricola degli studenti che hanno un voto superiore alla media generale sono:", matricola_voto_maggiore_media)
