class LinkedList:
    def __init__(self):
        self.head=ListNode()

    def printlist(self):
        temp=self.head.next
        while(temp!=None):
            print(temp.value,end=' ')
            temp=temp.next
        print(' ')

    def insert(self,x,p):
        a=p.next
        p.next=ListNode()
        p.next.value=x
        p.next.next=a

    def len(self):
        p=self.head
        count=0
        while p.next!=None:
            count=count+1
            p=p.next
        return count

    def delete(self,p):
        p.next=p.next.next

    def isEmpty(self):
        if self.head.next==None:
            return True
        else:
            return False

    def insertAtIndex(self,x,i):
        temp=self.head
        j=0
        while j<=i-1:
            temp=temp.next
            j+=1
        t=temp.next
        temp.next=ListNode()
        temp.next.value=x
        temp.next.next=t

    def search(self,x):
        t=self.head.next
        while t.next!=None:
            if t.value==x:
                return t
            else:
                t=t.next
        return None


class ListNode:
    def __init__(self):
        self.value=0
        self.next=None

def main():
    L=LinkedList()
    L.insert(10,L.head)
    print('list is')
    L.printlist()
    L.insert(12,L.head.next)
    print('List is')
    L.printlist()
    L.insert(2,L.head)
    print('list is')
    L.printlist()
    print('size is',L.len())
    L.delete(L.head)
    print('List is empty?',L.isEmpty())
    print('Size of L is ',L.len())
    L.insertAtIndex(2,0)
    L.insertAtIndex(1,0)
    L.insertAtIndex(4,2)
    L.insertAtIndex(3,2)
    print('list is')
    L.printlist()
    print('found  at',L.search(15))

if __name__ == '__main__':
    main()

