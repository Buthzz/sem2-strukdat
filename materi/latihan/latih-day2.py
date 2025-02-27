def stack():
    s=[]
    return (s)
def push(s,data):
    s.append(data)
def pop(s):
    data=s.pop()
    return(data)
def peek(s):
    return(s[len(s)-1])
def isEmpty(s):
    return (s==[])
def size(s):
    return(len(s))

# Latihan 1
def reverseWord(word):
    data = stack()
    # vokal = {'a', 'i', 'u', 'e', 'o'}

    for ch in word:
        # if ch not in vokal:
        push(data, ch)

    temp = ''
    while not isEmpty(data):
        temp += pop(data)

    return temp

print(reverseWord("Fajar"))