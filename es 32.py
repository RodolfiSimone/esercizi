'''implementa un algoritmo di calcolo della soluzione di un'equazione di primo grado a x + b = 0'''

numero_a = float(input("inserire il valore di a "))
numero_b = float(input("inserire il valore di b "))
if numero_a == 0 and numero_b == 0:
    print("l'equazione è indeterminata")
elif numero_a != 0 and numero_b == 0:
    print(" x = 0") 
elif numero_a == 0 and numero_b != 0:
    print("l'equazione è impossibile")
else:
    print("x =", -(numero_b/numero_a))