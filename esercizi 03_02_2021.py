'''Si definisca una funzione che preso un dizionario di studenti e voti, restituisca un dizionario con gli studenti suddivisi per 
  intervalli di media di voto,la lode permette di arrotondare all’intero successivo, nel caso in cui nella lista dei voti non sia
  presente una lode l’arrotondamento è per difetto
'''

def medie(dizionario):
    media_nome = {}
    for chiave in dizionario:
        valori = []
        if len(dizionario[chiave]) == 4:
            dizionario[chiave]. remove("Lode")
            media = round(sum(dizionario[chiave])/3)
        else:
            media = int(sum(dizionario[chiave])/3)
            
        if media in range(18,24):
            valori.append(chiave)
            try:
                valori.append(media_nome["18-23"])
            except:
                pass
            media_nome["18-23"] = valori
            
        elif media in range(24,28):
            valori.append(chiave)
            try:
                valori.append(media_nome["24-27"])
            except:
                pass
            media_nome["24-27"] = valori
            
        elif media in range(28,31):
            valori.append(chiave)
            try:
                valori.append(media_nome["28-30"])
            except:
                pass
            media_nome["28-30"] = valori
    
    for chiave in media_nome:
        print("gli studenti con media compresa tra", chiave, "sono:")
        print(*media_nome[chiave], sep = ", ") 


def main():
    lode = ()
    nome_media = {}
    while True:
        nome = input("inserire il nome dell'alunno: ").capitalize()
        voti = input("inserire i 3 voti, compresa la lode, separati da uno spazio: ").split()
        voti = [e.upper() for e in voti]
        while len(voti) >= 4:
            voti.remove("LODE")
            lode = True
            
        voti = [int(e) for e in voti]
        if lode:
            voti.append("Lode")

        nome_media[nome] = voti
        controllo = input("Scrivere 'si' se si vuole continuare ad inserire voti altrimenti inserire 'no' ")
        if controllo == "no":
            break
    medie(nome_media)


main()
