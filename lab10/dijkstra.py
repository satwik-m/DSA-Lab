class AdjLst:
	def __init__(self,v):
		self.ver=v
		self.head=[ListNode() for i in range(v)]
		#self.time=0
		for i in range(v):
			self.head[i].value=i
	
	def form(self,a,b,c):
		t=ListNode()
		t.value=b
		t.next=self.head[a].next
		self.head[a].next=t
		t.weight=c

	def printlst(self):
		for k in range(self.ver):
			print("vertex",k,end=" : ")
			t=self.head[k]
			while(t.next):
				print(t.next.value,end=" ")
				t=t.next
			print()

	def Dijkstra(self,s):
		self.head[s].dist=0
		H=BinaryMinHeap()
		for i in range(len(self.head)):
			H.insert(self.head[i])
		while(not H.isEmpty()):
			w=H.extractMin()
			t=w.next
			while(t):
				if self.head[t.value].dist>w.dist+t.weight:
					self.head[t.value].pred=w
					self.head[t.value].dist=w.dist+t.weight
					H.updatePriority(self.head[t.value])
				t=t.next

	def printlst(self,s):
		for i in range(len(self.head)):
			print("vertex:",i,"	",self.head[i].dist,end='  ')
			print("path:",end='  ')
			if self.head[i].dist!=float('inf'):
				self.getPath(self.head[i])
			else:
				print('no path exists')
			print()

	def getPath(self,t):
		if t==None:
			return
		self.getPath(t.pred)
		print(t.value,end=' ')

class BinaryMinHeap:
	def __init__(self):
		self.E=[]
		self.E.append(-999)
		self.l=len(self.E)
		
	def heapify(self,i):
		if (i<=(self.l-1)/2) and (i>0):
			if(2*i+1<self.l):
				t2=self.E[2*i+1].dist
			t1=self.E[2*i].dist
			if (2*i+1<self.l) and (self.E[i].dist>t2) and (t1>t2):
				t=self.E[2*i+1]
				self.E[2*i+1]=self.E[i]
				self.E[i]=t
				k=i*2+1
			elif(self.E[i].dist>t1):
				t=self.E[2*i]
				self.E[2*i]=self.E[i]
				self.E[i]=t
				k=2*i
			else:
				k=-1
			self.heapify(k)

	def BuildHeap(self):
		for i in range(int((self.l-1)/2),0,-1):
			self.heapify(i)

	def extractMin(self):
		t=self.E[1]
		self.E[1]=self.E[self.l-1]
		self.E[self.l-1]=t
		t=self.E[self.l-1]
		del self.E[self.l-1]
		self.l-=1
		self.heapify(1)
		return t

	def minimum(self):
		return self.E[1]

	def insert(self,k):
		self.l+=1
		self.E.append(k)
		i=int((self.l-1)/2)
		while i>0:
			self.heapify(i)
			i=int(i/2)

	def isEmpty(self):
		if len(self.E)==1:
			return True
		return False

	def updatePriority(self,t):
		for i in range(len(self.E)):
			if(self.E[i]==t):
				break
		self.E[i].dist=t.dist
		k=i
		while(k>0):
			self.heapify(int(k))
			k=k/2

class ListNode:
	def __init__(self):
		self.value=None
		self.next=None
		self.col='white'
		self.dist=float('inf')
		self.pred=None
		self.weight=None
		#self.start=-1
		#self.end=-1

def main():
	v=int(input("enter the no. of vertices:"))
	L=AdjLst(v)
	print("give input as: start end weight:")
	ch='y'
	while ch!='n':
		l=input().split()
		a=int(l[0])
		b=int(l[1])
		w=int(l[2])
		L.form(a,b,w)
		ch=input('do u want more edges(y/n)? ')
	#L.printlst()
	s=int(input("enter the source vertex to apply Dijkstra's:"))
	if s<v:
		L.head[s].dist=0
		#print("vertex order")
		L.Dijkstra(s)
		L.printlst(s)
	else:
		print("vertex doesnot exist in given graph")

if __name__ == '__main__':
	main()