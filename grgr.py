n = int(input("Numarul dorit:"))
s1 = 0
s2 = 0
for k in range (1, n + 1):
    s1 += k ** 3
for k in range (1, n + 1):
    s2 += k
s2 = s2 ** 2
print("s1 = ", s1)
print("s2 = ", s2)
if s1 > s2:
    print("s1 > s2")
elif s2 > s1:
    print("s2 > s1")
else:
    print("s1 = s2")

n = int(input("Numarul dorit:"))
s1 = 0
s2 = 0
for h in range (1, n + 1):
    s1 += h ** 2
s1 = 3 * s1
print("s1 = ", s1)
for h in range (1, n + 1):
    s2 += h
s2 = n ** 3 + n ** 2 + s2
print("s2 = ", s2)
if s1 > s2:
    print("s1 > s2")
elif s2 > s1:
    print("s2 > s1")
else:
    print("s1 = s2")