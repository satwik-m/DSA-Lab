class ParseTree():
	def __init__(self):
		self.root=TreeNode()

	def inputtree(self):
		s=input("enter the valid parenthesised expression:")
		L=list(s)
		l=len(L)
		t=self.root
		for i in L:
			if i=='(':
				k=TreeNode()
				t.left=k
				k.parent=t
				t=t.left

			elif i==')':
				t=t.parent

			elif i.isalnum():
				t.data=i
				t=t.parent

			else:
				t.data=i
				k=TreeNode()
				t.right=k
				k.parent=t
				t=t.right

	def preorder_traverse(self,p):
		t=p
		if(t==None):
			return
		else:
			print(t.data,end=" ")
			self.preorder_traverse(t.left)
			self.preorder_traverse(t.right)

	def postorder_traverse(self,p):
		t=p
		if(t==None):
			return
		else:
			self.postorder_traverse(t.left)
			self.postorder_traverse(t.right)
			print(t.data,end=" ")

	def evaluateTree(self,p):
		t=p
		if (t==None) or (t.left==None):
			return t.data
		else:
			op1=self.evaluateTree(t.left)
			op2=self.evaluateTree(t.right)
			op=t.data
			if(op=='+'):
				return int(op1)+int(op2)
			elif(op=='-'):
				return int(op1)-int(op2)
			elif(op=='*'):
				return int(op1)*int(op2)
			elif(op=='/'):
				return int(op1)/int(op2)


class TreeNode():
	def __init__(self):
		self.left=None
		self.right=None
		self.data=None
		self.parent=None

def main():
	pt=ParseTree()
	pt.inputtree()
	print("preorder traversal:")
	pt.preorder_traverse(pt.root)
	print()
	print("postorder traversal:")
	pt.postorder_traverse(pt.root)
	print()
	print("value=",pt.evaluateTree(pt.root))


if __name__ == '__main__':
	main()