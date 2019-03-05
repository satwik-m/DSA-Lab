#to print first n fibonacci numbers

def ifibo(n):
	a=0
	b=1
	print(a,'\n',b)
	for i in range(1,n-1):
		c=a+b
		print(c,' ')
		a=b
		b=c
	return

def rfibo(n,a,b,i):
	c=a+b
	print(c)
	i=i+1
	a=b
	b=c
	if i==n:
		return
	else:
	    rfibo(n,a,b,i)

n=int(input('how many fibonacci numbers do u want??\n'))
ifibo(n)
print('\n\n')
print(0)
print(1)
rfibo(n,0,1,2)


