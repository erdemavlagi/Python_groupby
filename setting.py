

ogrenciler =  [ "jonh", "mary", "erdem", "esra", "gizem","avlağı"]

A = []
B = []

for index, ogrenci in enumerate(ogrenciler):
    if index % 2 == 0:
        A.append(ogrenci)
    else:
        B.append(ogrenci)


print("A Grubu ",A)

print("B grubu ", B)