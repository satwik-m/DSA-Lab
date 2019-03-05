#sorting using bubble and selection sorts

n=int(input('enter the size of array'))
print('enter the elements of list')
L=[]
for i in range(0,n):
	L=L+[int(input())]
M=L
for j in range(0,n-1):
	for k in range(0,n-j-1):
		if L[k]>L[k+1]:
			t=L[k]
			L[k]=L[k+1]
			L[k+1]=t
print('bubble sort\n',L)

for i in range(0,n):
	a=M[i]
	for j in range(i,n):
		if a<M[i]:
			t=a
			a=M[i]
			M[i]=t
print('selection sort\n',M)

