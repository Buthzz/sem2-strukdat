# for i in range(5):
#     print(i)
#
# for i in range(2, 10, 2):
#     print(i)

# var_string = "Informatika"
# for i in var_string:
#     print(i)
#
# kondisi_awal = input("mulai/tidak? ")
# jawab = True
# while jawab and kondisi_awal == "mulai":
#     jawab = input("Apakah mau lanjut?")
#     if jawab == "y":
#         jawab = True
#     else:
#         jawab = False

for i in range(4):
    print(f"iterasi i ke - {i}")
    for j in range(3):
        print(f"iterasi j ke - {j}")


##### Built in data strcture #####

# String
var_string = "Algoritma"
print(var_string[3])
print(var_string[0:4])
print(var_string[0:9:2])

var_new = " Pemrograman"
# print(var_string + var_new)

for i in range(len(var_new)):
    var_string = var_string + var_new[i]

print(var_string)

# Penambahan
var_list = [1, "alpro", "strukdat"]
var_list2 = [True, False]
var_list.append(6)

var_list.insert(2, "DPW")
print(var_list)

var_list.extend(var_list2)
print(var_list)

# Penghapusan

var_list.pop(1) #hapus by index
print(var_list)

var_list.remove("strukdat") #hapus by isinnya
print(var_list)

# dictionary

tes = {
    "halo" : {
        "tes"
    }
}

print(tes)

#func
def luas_lingkaran(jari_jari=4):
    pi = 22/7
    rumus = pi*jari_jari**2
    return rumus

print(luas_lingkaran())