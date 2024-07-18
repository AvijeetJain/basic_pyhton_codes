l=[2,5,7,4,2,6,9,1]

for i in range(len(l)-1,-1,-1):
    for j in range(i):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
    print("Iteration", i,":",l)
        
