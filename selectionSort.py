l=[9,2,5,7,8,4,3,5,6,7]

for i in range(len(l)):
    min=i
    for j in range(i+1,len(l)):
        if l[min]>l[j]:
            min=j
    l[i], l[min]=l[min], l[i]
    for i in range(len(l)):
        print(l[i], end=' ')
    print()
