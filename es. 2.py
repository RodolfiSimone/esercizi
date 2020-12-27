'''Data la lista a che contiene n parole restituisca in output una lista di interi che rappresentano la lunghezza delle parole in a'''

a = input("lista parole, separate da uno spazio ").split()
b = []
for n in range (len(a)):
    parola = a[n]
    b.append(len(parola))
print("le loro lunghezze: ", b)