class Trie:
	def __init__(self):
		self.root=TrieNode()

	def Index(self,ch):
		return ord(ch)-ord('a')

	def insert(self,key):
		t=self.root
		l=len(key)
		for c in key:
			i=self.Index(c)
			if not t.children[i]:
				t.children[i]=TrieNode()
			t=t.children[i]

	def search(self,key):
		t=self.root
		l=len(key)
		count=0
		for c in key:
			i=self.Index(c)
			if not t.children[i]:
				return
			t=t.children[i]
		if t!=None:
			for i in range(26):
				if t.children[i]==None:
					count=count+1
			if count!=26:
				return "not found"
		if t!=None:
			return t
		else:
			return "not found"

class TrieNode:
	def __init__(self):
		self.children=[None]*26

def main():
	T=Trie()
	S=input("enter the keys to be inserted:")
	l=S.split()
	for i in l:
		T.insert(i)
	s=input("enter the key to search:")
	print(T.search(s))
	
if __name__ == '__main__':
	main()