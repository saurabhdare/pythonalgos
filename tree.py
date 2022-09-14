class Node(object):
    def __init__(self, item=None, level=0):
        self.item = item
        self.level = level
    
        # empty node
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return '{}'.format(self.item)

    def addNode(self, value, level_here=1):
        new_node = Node(value, level_here)

        if not self.item:
            self.item = new_node
        elif not self.left:
            self.left = new_node
        elif not self.right:
            self.right = new_node
        else:
            self.left = self.left.addNode(value, level_here + 1)
        return self

    def searchNode(self, value):
        if self.item == value:
            return self
        else:
            found = None
            if self.left:
                found = self.left.searchNode(value)
            if self.right:
                found = found or self.right.searchNode(value)
            return found

    def isLeaf(self):
        return not self.right and not self.left

    def getMaxHeight(self):
        levelr, levell = 0, 0
        if self.right:
            levelr = self.right.getMaxHeight() + 1
        if self.left:
            levell = self.left.getMaxHeight() + 1
        return max(levelr, levell)

    def getMinHeight(self, level=0):
        levelr, levell = -1, -1
        if self.right:
            levelr = self.right.getMinHeight(level + 1)
        if self.left:
            levell = self.left.getMinHeight(level + 1)
        return min(levelr, levell) + 1

    def isBalanced(self):
        if self.getMaxHeight() - self.getMinHeight() < 2:
            return False
        else:
            if self.isLeaf():
                return True
            elif self.left and self.right:
                return self.left.isBalanced() and self.right.isBalanced()
            elif not self.left and self.right:
                return self.right.isBalanced()
            elif not self.right and self.left:
                return self.left.isBalanced()
    
    def isBST(self, mintree=None, maxtree=None):
        ''' Whether the tree is Binary Search Tree or NOT'''
        if self.item:
            if not mintree:
                mintree = self.item
            if not maxtree:
                maxtree = self.item
            
            if self.isLeaf():
                return True
            elif self.left:
                if self.left.item < self.item and mintree > self.left.item:
                    mintree = self.left.item
                    return self.left.isBST(mintree, maxtree)
                else:
                    return False
            elif self.right:
                if self.right.item > self.item and maxtree < self.right.item:
                    maxtree = self.right.item
                    return self.right.isBST(mintree, maxtree)
                else:
                    return False
            else:
                print("Tree is empty")

class BTree(object):
    def __init__(self):
        self.root = None

    def addNode(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self.root.addNode(value)

    def isLeaf(self, value):
        node = self.root.searchNode(value)
        return node.isLeaf()

    def getNodeLevel(self, item):
        node = self.root.searchNode(item)
        if node:
            return node.level
        else:
            raise Exception('None not found')
    
    def isRoot(self, value):
        return self.root.item == value
    
    def getHeight(self):
        return self.root.getMaxHeight()
    
    def isBalanced(self):
        return self.root.isBalanced()

    def isBST(self):
        return self.root.isBST()

    def inorder(self):
        current = self.root
        nodes, stack = [], []
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                nodes.append(current.item)
                current = current.right
        return nodes

if __name__ == '__main__':
    bt = BTree()
    for i in range(1, 10):
        bt.addNode(i)

    print("What's the height of the tree? ", bt.getHeight())
    print("Is this tree a Binary Search Tree? ", bt.isBST())
    print(bt.inorder())
