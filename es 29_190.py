'''scrivere un programma che calcoli l'aliquota sul reddito inserito e la sua percentuale sul totale'''

limiti = [0, 15000, 28000, 55000, 75000, 10**12]
aliquota = [0, 23, 27, 38, 41, 43]
while True:
    reddito = float(input("Inserire il proprio reddito di cui si vuole calcolare l'aliquota "))
    imposta = 0
    for i in range(len(limiti)):
        if reddito > limiti[i]:
            imposta = imposta + (aliquota[i]/ 100)*(limiti[i]-limiti[i-1])
        else:
            imposta = imposta + (aliquota[i]/ 100)*(reddito-limiti[i-1])
            break
    perc_imposta = round((imposta*100)/reddito, 2)
    
    print("L'imposta totale è di", imposta, "quindi in percentuale sul reddito è", perc_imposta,"%")
    controllo = input("Inserire 'si' per un nuovo calcolo di reddito, inserire 'no', per chiudere il programma ")
    if controllo == "no":
        break
