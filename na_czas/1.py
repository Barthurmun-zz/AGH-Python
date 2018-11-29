class tree:
    def __init__(self,root):
        self.root = root
        self.lchild = None
        self.rchild = None
    
    def insert(self,newVal):
        if self.root:
            if newVal < self.root:
                if self.lchild is None:
                    self.lchild = tree(newVal)
                else:
                    self.lchild.insert(newVal)
            elif newVal > self.root:
                if self.rchild is None:
                    self.rchild = tree(newVal)
                else:
                    self.rchild.insert(newVal)
        else:
            self.root = newVal
    
    def printTree(self):
        print (self.root)
        if self.lchild:
            self.lchild.printTree()
        
        if self.rchild:
            self.rchild.printTree()

       
def traverse(tree):
    if tree:
        print (tree.root)
        if tree.lchild:
            print (tree.lchild)
            traverse(tree.lchild)
        elif tree.rchild:
            print (tree.rchild)
            traverse(tree.rchild)


if __name__ == "__main__":
    x = tree(10)
    x.insert(5)
    x.insert(30)
    x.insert(1)
    x.insert(7)
    x.insert(20)
    x.insert(40)    

    x.printTree()
    #traverse(x)