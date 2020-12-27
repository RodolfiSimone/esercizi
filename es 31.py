'''Fornisci la rappresentazione in binario di un numero decimale confrontandola con il valore ottenuto dalla funzione'''

numero_decimale = int(input("Inserire numero decimale "))
resto = 0
numero_binario = ""
numero_binario2 = bin(numero_decimale)
while True:
    if numero_decimale == 0:
        break
    resto = str(numero_decimale%2)
    numero_decimale = int(numero_decimale / 2)
    numero_binario = resto + numero_binario

print("Ecco il confronto dei risultati di due metodi per trasformare decimale in binario",numero_binario,"e", numero_binario2)