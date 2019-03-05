class AVL:
    def __init__(self):
        self.root = Node()

    def search(self, k, x):
        if x == None:
            return None
        elif k == x.key:
            return x
        elif k < x.key:
            x = x.left
            return self.search(k, x)
        else:
            x = x.right
            return self.search(k, x)
        return None

    def minimum(self, x):
        while x.left != None:
            x = x.left
        return x

    def maximum(self, x):
        while x.right != None:
            x = x.right
        return x

    def successor(self, x):
        if x.right != None:
            return self.minimum(x.right)
        y = x.parent
        while x != y.left and y != None:
            x = y
            y = y.parent
        return y

    def predecessor(self, x):
        if x.left != None:
            return self.maximum(x.left)
        y = x.parent
        while x != y.right and y != None:
            x = y
            y = y.parent
        return y

    def insert(self, k, x):
        if k < x.key and x.left != None:
            x = x.left
            return self.insert(k, x)

        if k > x.key and x.right != None:
            x = x.right
            return self.insert(k, x)

        if k < x.key and x.left == None:
            x.left = Node()
            x.left.key = k
            x.left.parent = x
            y=x.left
            self.rotate(x,y)
            return

        if k > x.key and x.right == None:
            x.right = Node()
            x.right.key = k
            x.right.parent = x
            y=x.right
            self.rotate(x,y)
            return

    def check(self, x):
        self.updateheight(x)
        if x.left == None and x.right == None:
            return 0

        if x.left != None and x.right == None:
            return x.left.height

        if x.left == None and x.right != None:
            return x.right.height

        if x.left != None and x.right != None:
            h = x.left.height - x.right.height
            if h < 0:
                return (-h)
            return h

    def height(self, x):
        if x == None:
            return 0
        return x.height

    def updateheight(self, x):
        if x==None:
            return
        x.height = max(self.height(x.left), self.height(x.right)) + 1

    def rotate(self, z,y):
        x = None
        while (self.check(z) <= 1):
            self.updateheight(z)
            x = y
            y = z
            z = z.parent

            if z == None:
                return

        if x == None or y == None:
            return

        if z.left == y and y.left == x:
            z.left = y.right
            y.right = z
            y.parent=z.parent
            z.parent=y
            self.updateheight(z)
            if z==self.root:
                self.root=y
                self.root.parent=None
            else:
                if y.parent.right==z:
                    y.parent.right=y
                else:
                    y.parent.left=y


        elif z.right == y and y.right == x:
            z.right = y.left
            y.left = z
            y.parent=z.parent
            z.parent=y
            self.updateheight(z)
            if z==self.root:
                self.root=y
                self.root.parent=None
            else:
                if y.parent.right==z:
                    y.parent.right=y
                else:
                    y.parent.left=y

        elif z.left == y and y.right == x:
            z.left = x.right
            y.right = x.left
            x.left = y
            x.right = z
            x.parent=z.parent
            z.parent=x
            y.parent=x
            self.updateheight(y)
            self.updateheight(z)
            self.updateheight(x)
            if z==self.root:
                self.root=x
                self.root.parent=None
            else:
                if x.parent.right==z:
                    x.parent.right=x
                else:
                    x.parent.left=x

        elif z.right == y and y.left == x:
            z.right = x.left
            y.left = x.right
            x.right = y
            x.left = z
            x.parent=z.parent
            z.parent=x
            y.parent=x
            self.updateheight(y)
            self.updateheight(z)
            self.updateheight(x)
            if z==self.root:
                self.root=x
                self.root.parent=None
            else:
                if x.parent.right==z:
                    x.parent.right=x
                else:
                    x.parent.left=x

    def drotate(self,z,y):
        x = None
        while (self.check(z) <= 1):
            y = z
            z = z.parent

            if z == None:
                return

        if z.left==y:
            y=z.right
        elif z.right==y:
            y=z.left
        if self.height(y.left)>self.height(y.right):
            x=y.left
        else:
            x=y.right

        oldh=z.height

        if z.left == y and y.left == x:    # rotations
            z.left = y.right
            y.right = z
            y.parent=z.parent
            z.parent=y
            self.updateheight(z)
            if z==self.root:
                self.root=y
                self.root.parent=None
            else:
                if y.parent.right==z:
                    y.parent.right=y
                else:
                    y.parent.left=y
            newroot=y

        elif z.right == y and y.right == x:
            z.right = y.left
            y.left = z
            y.parent=z.parent
            z.parent=y
            self.updateheight(z)
            if z==self.root:
                self.root=y
                self.root.parent=None
            else:
                if y.parent.right==z:
                    y.parent.right=y
                else:
                    y.parent.left=y
            newroot=y

        elif z.left == y and y.right == x:
            z.left = x.right
            y.right = x.left
            x.left = y
            x.right = z
            self.updateheight(y)
            self.updateheight(z)
            self.updateheight(x)
            x.parent=z.parent
            z.parent=x
            y.parent=x
            if z==self.root:
                self.root=x
                self.root.parent=None
            else:
                if x.parent.right==z:
                    x.parent.right=x
                else:
                    x.parent.left=x
            newroot=x

        elif z.right == y and y.left == x:
            z.right = x.left
            y.left = x.right
            x.right = y
            x.left = z
            self.updateheight(y)
            self.updateheight(z)
            self.updateheight(x)
            x.parent=z.parent
            z.parent=x
            y.parent=x
            if z==self.root:
                self.root=x
                self.root.parent=None
            else:
                if x.parent.right==z:
                    x.parent.right=x
                else:
                    x.parent.left=x
            newroot=x

        if oldh!=newroot.height:
            self.drotate(newroot,None)

    def delete(self, k):
        x = self.search(k, self.root)
        if x==None:
            return
        
        if x.left == None and x.right == None:
            z=x.parent
            if x == x.parent.left:
                x.parent.left = None
            else:
                x.parent.right = None
            self.drotate(z,None)
        else:
            if x.left == None and x.right != None:
                z=x.right
                x.right.parent = x.parent
                if x == x.parent.left:
                    x.parent.left = x.right
                else:
                    x.parent.right = x.right
                self.drotate(z,None)
            if x.left != None and x.right == None:
                z=x.left
                x.left.parent = x.parent
                if x == x.parent.left:
                    x.parent.left = x.left
                else:
                    x.parent.right = x.left
                self.drotate(z,None)
            if x.left != None and x.right != None:
                y = self.minimum(x.right)
                z = y
                x.key = y.key
                if y.parent.left == y:
                    y.parent.left = y.right
                else:
                    y.parent.right = None
                y.parent=None
                self.drotate(z,None)

    def preorder_traverse(self, p):
        t = p
        if (t == None):
            return
        else:
            print(t.key," ",t.height)
            self.preorder_traverse(t.left)
            self.preorder_traverse(t.right)


class Node:
    def __init__(self):
        self.parent = None
        self.key = None
        self.left = None
        self.right = None
        self.height = 1


def main():
    Tree = AVL()
    n = int(input('enter the number of values to be inserted '))
    Tree.root.key = int(input('enter a number '))
    for i in range(n - 1):
        a = int(input('enter a number '))
        Tree.insert(a, Tree.root)
    Tree.preorder_traverse(Tree.root)
    Tree.delete(25)
    #Tree.delete(9)
    print()
    Tree.preorder_traverse(Tree.root)


if __name__ == '__main__':
    main()
