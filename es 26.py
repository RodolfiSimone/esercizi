'''Calcola la media degli stipendi deid ipendenti di un'azienda fino a quando si inserisce il valore -1'''

n = 0
somma_stipendio = 0
while True:
    n +=1
    print("stipendio", n, "dipendente")
    stipendio = int(input())
    if stipendio == -1:
        break
    somma_stipendio = somma_stipendio + stipendio
    media_stipendio = somma_stipendio / n

print("la media degli stipendi è", media_stipendio)