def even(n):
	return n%2 ==0
L= [1,2,3,4,5,6,7,8,9]
Ev= [n for n in L if n % 2==0]
Evp = [n for n in L if even(n) ]
print (Evp)
