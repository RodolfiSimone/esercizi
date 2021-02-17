'''dato il fatturato di ogni zona in cui un'azienda vende calcola il fatturato totale e la percentuale di ogni zona sul totale'''


fatturato = input("Inserire il fatturato di ogni zona separato da uno spazio ").split()
fatturato_tot = 0
fatturato_perc = list()
for i in range(4):
    fatturato[i] = float(fatturato[i])
    fatturato_tot = fatturato_tot + fatturato[i]
for i in range(4):
    fatturato_perc.append(round((fatturato[i]*100)/fatturato_tot, 2))

print("Il fatturato totale è di", fatturato_tot, "in percentuale sul totale le rispettive zone sono", fatturato_perc)
