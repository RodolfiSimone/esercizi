'''Inserire uno alla volta i nomi dei pazienti in coda e poi restituire il nome del primo in lista '''

coda = []
while True:
    nome = str(input("Inserire il nome del paziente, in ordine di arrivo "))
    coda.append(nome.capitalize())
    controllo = str(input("Scrivere 'si' se vogliono inserire altri pazienti altimenti 'no' "))
    if controllo == "no":
        break

numero_pazienti = len(coda)
for n in range(numero_pazienti):
    print(coda.pop(0))
    if n == numero_pazienti-1:
        print("I pazienti sono terminati !!!")
    else:
        perdi_tempo = input("Premere Invio per visualizzare il paziente ssuccessivo ")
