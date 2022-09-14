class NodeBST(object):
    def __init__(self, item=None, level=0):
        self.item = item
        self.level = level
    
        # empty node
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return '{}'.format(self.item)

    def addNodeBST(self, value, level_here=1):
        new_node = NodeBST(value, level_here)

        if not self.item:
            self.item = new_node
        else:
            if value > self.item:
                self.right = self.right and self.right.addNodeBST(value, level_here + 1) or new_node
            elif value < self.item:
                self.left = self.left and self.left.addNodeBST(value, level_here + 1) or new_node
            else:
                print("BSTs do not support repeated items.")
            return self

    def searchForNode(self, value):
        if self.item == value:
            return self
        elif self.left and value < self.item:
            return self.left.searchForNode(value)
        elif self.right and value > self.item:
            return self.right.searchForNode(value)
        else:
            return False

class BSTree(object):
    def __init__(self):
        self.root = None

    def addNode(self, value):
        if not self.root:
            self.root = NodeBST(value)
        else:
            self.root.addNodeBST(value)

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

if __name__ == "__main__":
    bst = BSTree()
    for i in range(1, 10):
        bst.addNode(i)

    print(bst.inorder())
