'''Una rubrica con nomi e rispettivi numeri telefonici, inserito il nome restituisce il numero e se non presente restituisce un messaggio'''

rubrica = dict()

while True:
    chiave_valore = input("inserire nome persona e numero di telefono separati da una virgola ").split(", ")
    chiave_valore[1] = int(chiave_valore[1])
    rubrica[chiave_valore[0]] = chiave_valore[1]

    fine = input("scrivere 'si', se si vogliono inserire altri numeri telefonici altrimenti scrivere 'no' ")
    if fine == "no":
        break

while True:
    nome = input("il nome della persona di cui si vuole il numero ")
    if nome in rubrica:
        print(rubrica[nome])
    else:
        print("il numero telefonico della persona inserita non è stato inserito ")

    fine = input("scrivere 'si', se si vogliono cercare altri numeri telefonici altrimenti scrivere 'no' ")
    if fine == "no":
        break
