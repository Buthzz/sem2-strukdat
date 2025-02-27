# print("Hellow World")
def stack():
    s = []
    return (s)


def push(s, data):
    s.append(data)


def pop(s):
    data = s.pop()
    return (data)


def peek(s):
    return (s[len(s) - 1])


def isEmpty(s):
    return (s == [])


def size(s):
    return (len(s))


# data = stack()
# print(isEmpty(data))
#
# push(data,100)
# push(data,23)
# push(data,34)
# pop(data)
# push(data,56)
# pop(data)
# print(data)

# Latihan 1
# def reverseWord(word):
#     data = stack()
#     # vokal = {'a', 'i', 'u', 'e', 'o'}
#
#     for ch in word:
#         # if ch not in vokal:
#         push(data, ch)
#
#     # temp = ''
#     # while not isEmpty(data):
#     #     temp += (data)
#
#     return data
#
# print(reverseWord("Fajar"))

def checkParentheses(strMat):
    data = stack()
    for ch in strMat:
        if ch == '(':
            push(data, ch)
        elif ch == ')':
            if isEmpty(data):
                return 'kelebihan kurung tutup'
            else:
                pop(data)
    if isEmpty(data):
        return True
    else:
        return 'Kelebihan kurung buka'

print(checkParentheses('5 x (4 + 5) / (3 + 2) x (10 - 8))'))

def parenthesesCheck(strMath):
    kurung = {')': '(', '}': '{', ']': '['}

    kurungBuka = kurung.values()
    kurungTutup = kurung.keys()
    temp = stack()
    matched = True
    for ch in strMath:
        if ch in kurungBuka:  # if ch in kurung.values()
            push(temp, ch)
    if ch in kurungTutup:  # if ch in kurung.keys()
        if isEmpty(temp):
            return 'Kelebihan kurung Tutup'
    else:
        tempKurung = pop(temp)
    if tempKurung == kurung[ch]:
        matched = matched and True
    else:
        matched = matched and False
    if not (isEmpty(temp)):
        return 'Kelebihan Kurung Buka'
    if matched == True:
        return 'OK'
    else:
        return 'Tidak Cocok kurungnya'
