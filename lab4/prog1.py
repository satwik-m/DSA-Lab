class HashTable:
	def __init__(self):
		self.L=[None for i in range(30)]

	def insert(self,key):
		i=0
		sum=0
		while i<len(key):
			sum=sum+ord(key[i])
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
			sum=sum+ord(key[i])
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

	def printlist(self):
		for i in range(30):
			temp=self.L[i]
			while(temp!=None):
				print(temp.value,end=' ')
				temp=temp.next
			print(' ')




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
	T.insert('cat')
	T.insert('bat')
	T.insert('ten')
	T.insert('act')
	T.insert('net')
	T.printlist()
	T.search('tac')

if __name__ == '__main__':
	main()


