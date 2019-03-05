class AdjList:
	def __init__(self,n):
		self.L=[None for i in range(n)]

	def insert(self,k1,k2):
		if self.L[k1]!=None:
			temp=self.L[k1]
		else:
			temp=None
		self.L[k1]=ListNode()
		self.L[k1].value=k2
		self.L[k1].next=temp

		if self.L[k2]!=None:
			temp=self.L[k2]
		else:
			temp=None
		self.L[k2]=ListNode()
		self.L[k2].value=k1
		self.L[k2].next=temp

	def printlist(self,n):
		for i in range(n):
			temp=self.L[i]
			print('vertex ',i,':',end=' ')
			while(temp!=None):
				print(temp.value,end=' ')
				temp=temp.next
			print(' ')




class ListNode:
    def __init__(self):
        self.value=0
        self.next=None



def main():
	v=int(input('enter the no. of vertices '))
	print('enter the edges')
	G=AdjList(v)
	AdjMatrix = [[0 for x in range(v)] for y in range(v)]
	ch='y'
	while ch!='n':
		s=input('')
		s=s.split()
		G.insert(int(s[0]),int(s[1]))
		AdjMatrix[int(s[0])][int(s[1])]=1
		AdjMatrix[int(s[1])][int(s[0])]=1
		ch=input('do u want more edges(y/n)?  ')
	print('adjacency list:')
	G.printlist(v)
	print('')
	print('Adjacency matrix:')
	for i in range(v):
		for j in range(v):
			print(AdjMatrix[i][j],end=' ')
		print('')






if __name__ == '__main__':
	main()