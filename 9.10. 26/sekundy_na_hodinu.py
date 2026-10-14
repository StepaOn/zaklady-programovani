pocet=int(input("Zadej počet sekund: "))
dny=pocet//86400
hodiny=(pocet%86400)//3600
minuty=(pocet%3600)//60
sekundy=(pocet%3600)%60
if dny>0:
    print(f"{dny} d {hodiny}:{minuty:02}:{sekundy:02}")
else:
    print(f"{hodiny}:{minuty:02}:{sekundy:02}")




"""zbytek=pocet%3600
print(f"{pocet//3600}:{zbytek//60:02}:{zbytek%60:02}")"""