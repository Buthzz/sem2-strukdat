nomer = [1, 5, 5, 8, 9, 10, 12]
frekuensi = {}

for num in nomer:
    if num in frekuensi:
          frekuensi[num] = frekuensi[num] + 1
    else:
        frekuensi[num] = 1

maksimal = 0
muncul = 0

for num, banyak in frekuensi.items():
    print(num, banyak)
    if banyak > maksimal:
        maksimal = banyak
        muncul = num

# print(muncul)
