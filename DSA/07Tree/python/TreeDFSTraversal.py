# part - 02 #
'''
We always say that left node must come before right node.
If we have 2 nodes        1
                        2   3
        There are 6 ways to print:
            - 1.      1, 2, 3 --> Valid (Pre-Order) -> Root is before left
            - 2.      1, 3, 2 --> Invalid (left is after right)
            - 3.      2, 1, 3 --> Valid (In-Order) -> Root is in mid
            - 4.      3, 1, 2 --> Invalid (left is after right)
            - 5.      3, 2, 1 --> Invalid (left is after right)
            - 6.      2, 3, 1 --> Valid (post-Order) -> Root is in the end
'''

class Node:
    def __init__(self, value, leftnode=None, rightNode=None):
        self.data = value
        self.left = leftnode
        self.right = rightNode

'''
root = Node(1)
root.left = Node(3)
root.right = Node(5)

root.left.left = Node(2)
root.left.right = Node(4)

root.right.right = Node(8)
'''

class Tree:
    def __init__(self, value):
        self.root = Node(value)
    
    def isRootNone(self):
        if (self.root is None):
            return True
        return False
    
    def nodeAddress(self, nodeVal):
        ''' return the address if node with nodeVal is available. We will be using BfFS here to cover all techniques.'''
        queue = []
        queue.append(self.root)
        nodeFound = None
        while(queue):
            temp_node = queue.pop(0)
            if (temp_node.data == nodeVal):
                nodeFound = temp_node
                break
            if (temp_node.left is not None):
                queue.append(temp_node.left)
            if (temp_node.right is not None):
                queue.append(temp_node.right)
        return nodeFound

    def addleftnode(self, oldNodeVal, newNodeVal, newNodeLeft=None, newNodeRight=None):
        if (self.isRootNone()):
            print("Tree is not available")
            return
        oldNode = self.nodeAddress(oldNodeVal)
        oldNode.left = Node(newNodeVal, newNodeLeft, newNodeRight)
        print("Node is successfully added")

    def addrightnode(self, oldNodeVal, newNodeVal, newNodeLeft=None, newNodeRight=None):
        if (self.isRootNone()):
            print("Tree is not available")
            return
        oldNode = self.nodeAddress(oldNodeVal)
        oldNode.right = Node(newNodeVal, newNodeLeft, newNodeRight)
    
    def preOrder(self, node, ans):
        ans.append(node.data)
        if (node.left is not None):
            self.preOrder(node.left, ans)
        if (node.right is not None):
            self.preOrder(node.right, ans)
    
    def inOrder(self, node, ans):
        if (node.left is not None):
            self.inOrder(node.left, ans)
        ans.append(node.data)
        if (node.right is not None):
            self.inOrder(node.right, ans)
    
    def postOrder(self, node, ans):
        if (node.left is not None):
            self.postOrder(node.left, ans)
        if (node.right is not None):
            self.postOrder(node.right, ans)
        ans.append(node.data)
    
    def printTree(self, dfsType='inorder'):
        ''' dfsType is inorder/preorder/postorder'''
        if (self.isRootNone()):
            print("Tree not available.")
            return
        ans = []
        if (dfsType == 'inorder'):
            self.inOrder(self.root, ans)
        elif (dfsType == 'preorder'):
            self.preOrder(self.root, ans)
        elif (dfsType == 'postorder'):
            self.postOrder(self.root, ans)
        else:
            print("dfsType is inorder/preorder/postorder")
            return
        print(f"{dfsType} traversal of Tree: ", end=" ")
        for nodeVal in ans:
            print(nodeVal, end=" ")
        print('\n')
    

tree1 = Tree(1)
tree1.addleftnode(1, 3)
tree1.addrightnode(1, 5)

tree1.addleftnode(3, 2)
tree1.addrightnode(3, 4)

tree1.addrightnode(5, 8)

tree1.printTree('preorder')
tree1.printTree('inorder')
tree1.printTree('postorder')