n=int(input("Dati numarul dorit:"))
s=0
y=1
for n in range(1, n+1):
    y*=n
    s+=y
print("1!+2!+3!+...+n!=", s)