vocali= [ "a", "e", "i" ,"o" , "u" ]
traduzioni = []

while True:
    parola = input("inserire parola da tradurre ")
    Testo = ""
    for lettera in parola:
        if lettera.lower() not in  vocali:
            Testo = Testo + lettera + "o" + lettera
        else:
            Testo = Testo + (lettera) 
    traduzioni.append(Testo)

    controllo = int(input("per inserire un'altra parola da tradurre inserire 1, per visualizzare la traduzione inserire 0 "))
    if controllo == 0:
        break
    
print (traduzioni)