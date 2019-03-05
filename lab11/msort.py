def mergesort(A,low,high):
	if low<high:
		mid=(low+high)//2
		mergesort(A,low,mid)
		mergesort(A,mid+1,high)
		merge(A,low,mid,high)

def merge(A,low,mid,high):
	l=0
	r=0
	L=[]
	R=[]
	for i in range(low,mid+1):
		L=L+[A[i]]
	for i in range(mid+1,high+1):
		R=R+[A[i]]
	i=low
	while (l<mid-low+1) and (r<high-mid):
		if L[l]>R[r]:
			A[i]=sR[r]
			r=r+1
		else:
			A[i]=L[l]
			l=l+1
		i=i+1
	if l<mid-low+1:
		while l<mid-low+1:
			A[i]=L[l]
			l=l+1
			i=i+1
	else:
		while r<high-mid:
			A[i]=R[r]
			r=r+1
			i=i+1

def main():
	L=[4,8,6,1,9,3,7,5]
	mergesort(L,0,len(L)-1)
	print(L)

if __name__ == '__main__':
	main()

