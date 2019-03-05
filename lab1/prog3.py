#to find whether the number is prime

x=int(input('enter a positive number'))
flag=1
if x<=1:
	print('false')
elif x==2:
	print('true')
else:
	for i in range(2,(int)(x/2)):
		if x%i==0:
		    flag=0
		    break
	if flag:
		print('true')
	else:
		print('false')