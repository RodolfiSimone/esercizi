'''Dato un elenco di città con nome, temperatura massima e minima di un giorno, conta quante città hanno superato l'escursione media'''

città = input("Nomi di ogni città separate da uno spazio: ").split()
numero = 0
massima = []
minima = []
escursione = []
for i in range(len(città)):
    temperatura_massima = int(input("La temperatura massima registrata in un giorno nella città corrispondente? "))
    temperatura_minima = int(input("La temperatura minima registrata in un giorno nella città corrispondente? "))
    massima.append(temperatura_massima)
    minima.append(temperatura_minima)
escursione_fissa = int(input("Escursione termica fissa: "))

for n in range(len(città)):
    differenza = massima[n] - minima[n]
    print("Le esursioni termiche sono: ", differenza)
    escursione.append(differenza)

for n in range(len(massima)):
    valore = escursione[n]
    if valore > escursione_fissa:
        numero += 1
print("Numero di città con escuscione termica più alta di quella fissa: ",numero)