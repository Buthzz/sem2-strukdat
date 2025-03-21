# radius=int(input('Masukkan nilai radius = '))
# luas=(22/7)*radius**2
# print('Luas lingkaran = ',luas)

# def factorial(num):
#     if num==0:
#         temp=1
#     else:
#         temp=1
#     while num>=1:
#         temp=temp*num
#         num=num-1
#     return(temp)
# # Main Program #
# a=int(input("Masukkan bilangan="))
# b=factorial(a)
# print (a,'!=',b)

kamar  = [10,9,7,2,1]
a = len(kamar)-1
# print(a)

for i in range(a, -1, -1):
    print(kamar[i])