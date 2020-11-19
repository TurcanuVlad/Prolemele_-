a = int(input("dati 1 latura: "))
b = int(input("dati 2 latura: "))
c = int(input("dati 3 latura: "))
if a<0 or c<0 or b<0:
    print("Latura nu poate avea lungimi negative")
elif a==b and b==c and c==a:
    print("Triunghi echilateral")
elif a!=b and b!=c and a!=c:
    print("Triunghi scalen")
elif (a==b and b!=c) or (b==c and c!=a) or (c==a and c!=b):
     print("Triunghi isoscel")
