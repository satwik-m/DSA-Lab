class stack:
	def __init__(self):
		self.p=[]
		self.top=None
	
	def push(self,x):
		self.p=self.p+[x]
		self.top=len(self.p)-1

	def pop(self):
		t=self.p[self.top]
		self.p.remove(self.p[self.top])
		self.top=self.top-1
		return t

def main():
	S=stack()
	str='12+84/6*-1+'
	l=len(str)
	i=0
	while i<l:
		if (str[i]=='+' or str[i]=='-' or str[i]=='*' or str[i]=='/'):
			a=S.pop()
			b=S.pop()
			if str[i]=='+':
				c=int(b)+int(a)
				S.push(c)
			if str[i]=='-':
				c=int(b)-int(a)
				S.push(c)
			if str[i]=='*':
				c=int(b)*int(a)
				S.push(c)
			if str[i]=='/':
				c=int(b)/int(a)
				S.push(int(c))
		else:
			S.push(str[i])
			
		i=i+1
	print('the value of given expression is ',S.pop())

if __name__ == '__main__':
	main()

