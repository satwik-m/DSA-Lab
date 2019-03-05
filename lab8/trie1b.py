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
		t.isEnd=True

	def search(self,key):
		t=self.root
		l=len(key)
		for c in key:
			i=self.Index(c)
			if not t.children[i]:
				return
			t=t.children[i]
		if t!=None and t.isEnd==True:
			return t
		else:
			return None

class TrieNode:
	def __init__(self):
		self.children=[None]*26
		self.isEnd=False

def main():
	T=Trie()
	S=input("enter the keys to be inserted:")
	l=S.split()
	for i in l:
		T.insert(i)
	s=input("enter the key to search:")
	t=T.search(s)
	if t==None:
		print('not found')
	else:
		print('found')
	


if __name__ == '__main__':
	main()