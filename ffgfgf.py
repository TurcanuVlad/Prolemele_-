n = int(input("Dati numarul dorit:"))
f=1
s=0
for x in range (1,n + 1):
    f*=x
    s+=f
    print(s)