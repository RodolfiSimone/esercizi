'''si acquisiscono i voti ottenuti da due candidati, comunica il vincitore e la sua percentuale di voti'''

voti_a = int(input("numero voti per il primo candidato"))
voti_b = int(input("voti per il seconcdo"))
percentuale_a = (voti_a/(voti_a + voti_b))*100
percentuale_b = (voti_b/(voti_a + voti_b))*100
print("percentuale candidato A" , int(percentuale_a),"%","percentuale candidato B", int(percentuale_b), "%")
if voti_a > voti_b:
    print("il vincitore è il candidato A")
elif voti_b > voti_a:
    print("il vincitore è il candidato B")
else:
    print("pareggio")