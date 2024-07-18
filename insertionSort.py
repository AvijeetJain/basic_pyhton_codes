l=[2,5,7,4,2,6,9,1]

for i in range(1,len(l)):
    a=l[i]
    j=i-1

    while j>=0 and a<l[j]:
        l[j+1]=l[j]
        j=j-1

    else: 
        l[j+1]=a
    print(i, l)
                
               
