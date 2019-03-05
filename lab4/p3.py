class LinkedList:
	def __init__(self):
		"""Create a new list with a Sentinel Node"""
		self.head=ListNode()
	def insert(self,x,p):
		"""Insert element x in the position after p"""
		temp=ListNode()
		temp.value=x
		temp.next=p.next
		p.next=temp
	def delete(self,p):
		"""Delete the node following node p in the linked list."""
		p.next=p.next.next
	def printlist(self):
		""" Print all the elements of a list in a row."""
		temp=self.head
		while temp.next != None:
			print(temp.next.value),
			temp=temp.next
	def insertAtIndex(self,x,i):
		"""Insert value x at list position i. (The position of the first element is taken to be 0.)"""
		t=self.head
		j=0
		if(j==i):
			temp=ListNode()
			temp.value=x
			temp.next=t.next
			t.next=temp
		else:
			t=t.next
			j+=1

	def search(self,x):
		"""Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
		temp=self.head
		while(temp.next !=None):
			if(temp.next.value == x):
				print(temp.next.value)
				break
			else:
				temp=temp.next
		if(temp.next == None):
			print("element not found")
	def len(self):
		"""Return the length (the number of elements) in the Linked List."""
		temp=self.head.next
		count=0
		while(temp != None):
			count+=1
			temp=temp.next
		return(count)
	def isEmpty(self):
		"""Return True if the Linked List has no elements, False otherwise."""
		temp=self.head
		if(temp.next == None):
			print("True")
		else:
			print("False")"""


class ListNode:
	def __init__(self,val=None,nxt=None):
		self.value=val
		self.next=nxt
class hash():
	def cs(self,str):
		h=0
		for i in range(len(str)):
			h=h+ord(str[i])*pow(33,i)
		h=h%30
		return(h)
	def suggest(self,str,T):
		h=self.cs(str)
		temp=T[h].head
		while(temp.next !=None):
			if(temp.next.value == str):
				"""print("string:",temp.next.value,"\nreference:",temp.next)
				print("hash index:",h)"""
				print(str)
				break
			else:
				temp=temp.next
	def inserth(self,p,str):
		temp=ListNode()
		temp.next=p.next
		temp.value=str
		p.next=temp
	def searchh(self,str,p):
		h=self.cs(str)
		temp=p
		while(temp.next !=None):
			if(temp.next.value == str):
				"""print("string:",temp.next.value,"\nreference:",temp.next)
				print("hash index:",h)"""
				print("string ",str," is valid")
				return 0
			else:
				temp=temp.next
		if(temp.next == None):
			print("invalid string")
			return 1
	def keys(self,p):
		for i in range(30):
			temp=p[i].head
			while temp.next != None:
				print(temp.next.value)
				temp=temp.next
def main():
	H=hash()
	T=[None for i in range(30)]
	for i in range(30):
		T[i]=LinkedList()
	S=[]
	f=open("ispell.dict","r")
	for line in f:
		S.append(line.strip())
	for i in range(len(S)):
		h=H.cs(S[i])
		H.inserth(T[h].head,S[i])
	str=input("enter a word(key) to search:")
	h=H.cs(str)
	s1=H.searchh(str,T[h].head)
	if s1==1:
		print("suggested words:")
		for i in range(len(str)):
			s=str
			for j in range(1,27):
				s=list(s)
				s[i]=chr(((ord(s[i])+1-97)%26)+97)
				s="".join(s)
				H.suggest(s,T)
	"""H.keys(T)"""
	f.close()
if __name__ == '__main__':
	main()