A = input("lista parole, separate da uno spazio ").split()
B = []
for n in range (len(A)):
    parola = A[n]
    B.append(len(parola))
print("le loro lunghezze: ", B)