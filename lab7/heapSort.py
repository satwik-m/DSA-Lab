class BinaryHeap:

	def __init__(self,A=None):
		if A is not None:
			self.L=[0]+A
		else:
			self.L=[0]
	

	def insert(self,x):
		#self.count+=1
		self.L.append(x)
		c=len(self.L)-1
		p=self.parent(child)
		
		while p>0:
			#print(x,self.L[parent])
			if self.L[p]<x:
				self.swap(p,c)
			c=p
			p=self.parent(p)

	def left(self,i):
		return 2*i
	
	def right(self,i):
		return 2*i+1
	
	def parent(self,i):
		return i//2
	
	def maximum(self):
		if len(self.L) != 1:
			return self.L[1]
		else:
			return "Error:Heap is Empty"

	def swap(self,x,y):
		temp=self.L[x]
		self.L[x]=self.L[y]
		self.L[y]=temp

	def max(self,x,y):
		if x>y:
			return x
		return y

	def heapify(self,start):
		
		root=start
		toSwap=None
		i=None
		
		if self.left(root)>(len(self.L)-1):
			return
		elif self.right(root)>(len(self.L)-1):
			toSwap=self.L[self.left(root)]
		else:
			toSwap=self.max(self.L[self.left(root)],self.L[self.right(root)])
		
		if self.L[root]<toSwap:
			if toSwap==self.L[self.left(root)]:
				i=self.left(root)
				self.swap(root,self.left(root))
			else:
				i=self.right(root)
				self.swap(root,self.right(root))
			self.heapify(i)

	
	def extractMax(self):
		if len(self.L)==1:
			return "Heap is empty"
		self.swap(1,len(self.L)-1)
		print(self.L.pop(),end=" , ")
		self.heapify(1)

	def printHeap(self):
		if len(self.L)==1: 
			print("Heap is empty")
			return
		print(self.L[1:])

	def buildHeap(self,A):
		self.L=[0]+A
		n=1
		n1=None
		while n<(len(self.L)-1):
			n1=n
			n=n*2

		for i in range(n1-1,0,-1):
			self.heapify(i)

	def sort(self):
		for i in range(1,len(self.L)):
			self.extractMax()


A=[1,4,10,5,10,13,12,11,2,23,21,32,42,26,16,14,9,-21]
print("Unsorted Array:\n",A)
heap=BinaryHeap()
heap.buildHeap(A)
print("Sorted Array:")
heap.sort()

