class BST:
	def __init__(self):
		self.root=Node()

	def search(self,k,x):
		if x==None:
			return None
		elif k==x.key:
			return x
		elif k<x.key:
			x=x.left
			return self.search(k,x)
		else:
			x=x.right
			return self.search(k,x)
		return None

	def minimum(self,x):
		while x.left!=None:
			x=x.left
		return x

	def maximum(self,x):
		while x.right!=None:
			x=x.right
		return x

	def successor(self,x):
		if x.right!=None:
			return self.minimum(x.right)
		y=x.parent
		while x!=y.left and y!=None:
			x=y
			y=y.parent
		return y

	def predecessor(self,x):
		if x.left!=None:
			return self.maximum(x.left)
		y=x.parent
		while x!=y.right and y!=None:
			x=y
			y=y.parent
		return y

	def insert(self,k,x):
		if k<x.key and x.left!=None:
			x=x.left
			return self.insert(k,x)

		if k>x.key and x.right!=None:
			x=x.right
			return self.insert(k,x)

		if k<x.key and x.left==None:
			x.left=Node()
			x.left.key=k
			x.left.parent=x
			return

		if k>x.key and x.right==None:
			x.right=Node()
			x.right.key=k
			x.right.parent=x
			return

	def delete(self,k):
		x=self.search(k,self.root)
		if x.left==None and x.right==None:
			if x==x.parent.left:
				x.parent.left=None
			else:
				x.parent.right=None
		else:
			if x.left==None and x.right!=None:
				x.right.parent=x.parent
				if x==x.parent.left:
					x.parent.left=x.right
				else:
					x.parent.right=x.right
			if x.left!=None and x.right==None:
				x.left.parent=x.parent
				if x==x.parent.left:
					x.parent.left=x.left
				else:
					x.parent.right=x.left
			if x.left!=None and x.right!=None:
				y=self.minimum(x.right)
				x.key=y.key
				if y.parent.left==y:
					y.parent.left=y.right
				else:
					y.parent.right=None




class Node:
	def __init__(self):
		self.parent=None
		self.key=None
		self.left=None
		self.right=None

def main():
	Tree=BST()
	n=int(input('enter the number of values to be inserted '))
	Tree.root.key=int(input('enter a number '))
	for i in range(n-1):
		a=int(input('enter a number '))
		Tree.insert(a,Tree.root)
	Tree.preorder_traverse(Tree.root)
	print('')
	Tree.delete(8)
	Tree.preorder_traverse(Tree.root)
	print('')
	x=Tree.search(20,Tree.root)
	if x!=None:
		print('found')
	else:
		print('not found')
	y=Tree.minimum(Tree.root)
	print(y.key)
	y=Tree.maximum(Tree.root)
	print(y.key)

	
if __name__ == '__main__':
	main()
