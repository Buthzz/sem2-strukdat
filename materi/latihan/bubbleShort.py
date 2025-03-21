def bubbleSort(listData):
    print('Data yang akan diurutkan : ', listData)
    count=0
    for outIter in range(len(listData)-1,-1,-1):
        print('outIter=',outIter)
        count=count+1
        print ('Iterasi ke-', count,':')
        for i in range(outIter):
            if listData[i]>listData[i+1]:
                temp=listData[i]
                listData[i]=listData[i+1]
                listData[i+1]=temp
                 #listData[i],listData[i+1]=listData[i+1],listData[i]
            print(outIter,'=',listData)
    print('Data urut-',listData)

a=[12,0,5,1,11,20,4,2]
bubbleSort(a)
b=[12,11,5,1,0]
print('--')
bubbleSort(b)