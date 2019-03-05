class GraphNode:
	def __init__(self):
		self.color='white'
		self.start=None
		self.end=None
		self.pred=None
		self.edge=[]

class AdjList:
	def __init__(self,n):
		self.L=[None for i in range(n)]
		for i in range(n):
			self.L[i]=GraphNode()
		self.visit=[]
		self.time=1
		self.Q=Queue()

	def insert(self,k1,k2):
		self.L[k1].edge=self.L[k1].edge+[k2]
		self.L[k2].edge=self.L[k2].edge+[k1]

	def printgraph(self,v):
		for i in range(v):
			print('vertex ',i,':',end=' ')
			print(self.L[i].edge)
			print(' ')

	def DFS(self,u):
		self.L[u].start=self.time
		self.time=self.time+1
		self.L[u].color='grey'
		self.Q.enqueue(u)
		for i in range(len(self.L[u].edge)):
			v=self.L[u].edge[i]
			if self.L[v].color=='white':
				self.DFS(v)
				self.L[v].pred=self.L[u]
		self.L[u].color='black'
		self.L[u].end=self.time
		self.time=self.time+1

class Queue:
	def __init__(self):
		self.l=[]

	def enqueue(self,v):
		self.l=self.l+[v]

	def dequeue(self):
		a=self.l.pop(0)
		return a

v=int(input('enter the no. of vertices '))
print('enter the edges')
G=AdjList(v)
ch='y'
while ch!='n':
	s=input('')
	s=s.split()
	G.insert(int(s[0]),int(s[1]))
	ch=input('do u want more edges(y/n)?  ')
s=int(input('enter the source vertex '))
G.DFS(s)
while len(G.Q.l)!=0:
	u=G.Q.dequeue()
	print(u,' timestamps -',G.L[u].start,' ',G.L[u].end)
