class AdjList:
	def __init__(self,n):
		self.L=[None for i in range(n)]
		for i in range(n):
			self.L[i]=GraphNode()
		self.visit=Queue()

	def insert(self,k1,k2):
		self.L[k1].edge=self.L[k1].edge+[k2]

	def printgraph(self,v):
		for i in range(v):
			print('vertex ',i,':',end=' ')
			print(self.L[i].edge)
			print(' ')

	def BFS(self,s):
		self.L[s].dist=0
		self.L[s].color='grey'
		Q=Queue()
		Q.enqueue(s)
		while len(Q.l)!=0:
			u=Q.dequeue()
			for i in range(len(self.L[u].edge)):
				v=self.L[u].edge[i]
				if self.L[v].color=='white':
					self.L[v].dist=self.L[u].dist+1
					self.L[v].color='grey'
					self.L[v].pred=self.L[u]
					Q.enqueue(v)
				if self.L[v]
			self.L[u].color='black'

class GraphNode:
	def __init__(self):
		self.color='white'
		self.dist='inf'
		self.pred=None
		self.edge=[]

class Queue:
	def __init__(self):
		self.l=[]

	def enqueue(self,v):
		self.l=self.l+[v]

	def dequeue(self):
		a=self.l.pop(0)
		return int(a)


v=int(input('enter the no. of vertices '))
print('enter the edges')
G=AdjList(v)
ch='y'
while ch!='n':
	s=input('')
	s=s.split()
	G.insert(int(s[0]),int(s[1]))
	ch=input('do u want more edges(y/n)?  ')
