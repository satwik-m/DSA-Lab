class HashTable:
	def __init__(self):
		self.L=[None for i in range(30)]

	def insert(self,key):
		i=0
		sum=0
		while i<len(key):
			sum=sum+((33**i)*ord(key[i]))
			i=i+1
		h=sum%30
		if self.L[h]!=None:
			temp=self.L[h]
		else:
			temp=None
		self.L[h]=ListNode()
		self.L[h].value=key
		self.L[h].next=temp

	def search(self,key):
		i=0
		sum=0
		while i<len(key):
			sum=sum+((33**i)*ord(key[i]))
			i=i+1
		h=sum%30
		t=self.L[h]
		while(t!=None):
			if(t.value==key):
				print('found')
				return
			else:
				t=t.next
		print('not found')




class ListNode:
    def __init__(self):
        self.value=0
        self.next=None

    def printlist(self):
        temp=self
        while(temp!=None):
            print(temp.value,end=' ')
            temp=temp.next
        print(' ')

def main():
	T=HashTable()
	F=open("small.dict","r")
	for line_terminated in F:
		line=line_terminated.rstrip('\n')
		T.insert(line)
	T.search('above')


if __name__ == '__main__':
	main()