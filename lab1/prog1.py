#to find the factorial

def ifactorial(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    return fact

def rfactorial(a):
    if a>1:
        return a*rfactorial(a-1)
    if a==1:
        return 1

x=int(input('enter a positve number'))
fact=ifactorial(x)
print('the factorial of',x,'is',fact)
fact1=rfactorial(x)
print('the factorial of',x,'is',fact1)

