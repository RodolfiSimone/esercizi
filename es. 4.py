figura = input("insrire il tipo di figura di cui si vuole calcolare l'area ").lower()
if figura == "triangolo" or "quadrato" or "rettangolo" or "cerchio":
    if figura == "cerchio":
        raggio = int(input("inserire il raggio "))
        area = (raggio**2)*3.14
    else:
        lato= int(input("inserire un lato "))
        altezza = int(input("inserire altezza "))
        area = lato*altezza        
        if figura == "triangolo":
            area = area/2
    print(area)

else:
    print("figura non valida")