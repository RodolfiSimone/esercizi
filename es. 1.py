'''Scrivi un programma che riconosce se la parola data è palindroma'''

parola = input("parola ")
if parola == parola[::-1]:
    print("la parola è palindroma")
else:
    print("la parola non è palindroma")