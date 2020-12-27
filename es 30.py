'''Fornisci la rappresentazione in decimale di un numero binario confrontandola con il valore ottenuto dalla funzione'''

numero_cifre = int(input("Da quante cifre è formato il tuo numero binario? "))
numero_binario = ""
numero_decimale = 0
for n in range(numero_cifre):
    print("cifra", n+1, "partendo da destra ")
    cifra = input()
    numero_binario = cifra + numero_binario
    cifra = int(cifra)
    numero_decimale = numero_decimale + (cifra*(2**n))

numero_decimale2 = int(numero_binario,2)
print("Ecco il confronto dei risultati di due metodi per trasformare binario in decimale",numero_decimale,"e",numero_decimale2 )