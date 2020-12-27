'''Un programma che scriva la differenza di a b se il loro prodotto è maggiore di 10 oppure la somma se il prodotto è minore di 10'''

a = int(input("inserire valore A "))
b = int(input("inserire valore B "))
p = a*b
if p>10:
    s = a-b
else:
    s = a+b
print(s)