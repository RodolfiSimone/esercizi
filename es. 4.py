'''scrivi un programma ceh a scelta dell'utente calcoli l'area di un quadrato, rettangolo, triangolo e cerchio'''

from math import pi

figura = input("insrire il tipo di figura di cui si vuole calcolare l'area ").lower()
if figura == "triangolo" or "quadrato" or "rettangolo" or "cerchio":
    if figura == "cerchio":
        raggio = float(input("inserire il raggio "))
        area = (raggio**2)*pi
    else:
        lato = float(input("inserire un lato "))
        altezza = float(input("inserire altezza "))
        area = lato*altezza        
        if figura == "triangolo":
            area = area/2
    print(area)

else:
    print("figura non valida")