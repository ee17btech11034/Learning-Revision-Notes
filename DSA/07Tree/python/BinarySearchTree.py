# part - 03
'''
BST => left node is always less than root and right node has val greater then root node.
TC=> log (n)  but if skewed then O(n).
'''

'''
    Deletion in BST:
        Terminologies:
            1. inOder Traversal:-> traversal of BST in [left-root-right] => 12 15 18 20 30 40 
            2. InOrder predecessor:
                    - InOrder predecessor of an element is the element that comes right before that element in InOrder traversal.
                            -> 15 is InOrder predecessor of 18
                    - in tree, go one step to left and then right most.  
            3. InOrder Successor: 
                    - InOrder Successor of an element is the element that comes right after that element in InOrder traversal.
                            -> 15 is InOrder Successor of 12
                    - in tree, go one step to right and then left most.

        Deletion case:
            1. case 1: Deletion of Lead Node:
                            -> If it has 0 child then, its parent must ref to None.
            2. Case 2: Deletion of having one child:
                            -> if we remove a node which has one child, then its child will be attached to its parent. 
                            -> If we solve case 2 then we do not have to explicitly write code for case 1. As if left node is not there then parent will refer to right child of node; if right is not available then left will be point.
            3. case 3; Deletion of node having 2 children:
                            -> Replace that node with either "InOrder predecessor" or "InOrder Successor".

'''
class Node:
    def __init__(self, value, leftNode=None, rightNode=None):
        self.data = value
        self.left = leftNode
        self.right = rightNode
    
class BST:
    def __init__(self, value):
        self.root = Node(value)
    
    def __insert(self, node, value):
        if (node is None):
            return Node(value)        
        if (node.data == value):
            return node
        elif (node.data > value):
            node.left = self.__insert(node.left, value)
        else:
            node.right = self.__insert(node.right, value)
        return node
    
    def insertNode(self, value):
        if (self.root is None):
            self.root = Node(value)
        else:
            self.root = self.__insert(self.root, value)
    
    def __inOrder(self, node, ans):
        if (node.left is not None):
            self.__inOrder(node.left, ans)
        ans.append(node.data)
        if (node.right is not None):
            self.__inOrder(node.right, ans)
    
    def printInOrder(self):
        ''' inorder traversal'''
        if (self.root is None):
            print("Tree not available.")
            return
        ans = []
        self.__inOrder(self.root, ans)
        print(f"In-Order traversal of Tree: ", end=" ")
        for nodeVal in ans:
            print(nodeVal, end=" ")
        print('\n')

    def __isNodePresent(self, node, value):
        if (node is None):
            return False
        nodeFound = False
        if (node.data == value):
            return True
        elif (node.data > value):
            nodeFound = nodeFound or self.__isNodePresent(node.left, value)
        elif (node.data < value):
            nodeFound = nodeFound or self.__isNodePresent(node.right, value)
        return nodeFound

    def lookupNode(self, value):
        nodeFound = self.__isNodePresent(self.root, value)
        if (nodeFound):
            print(f"node with value {value} is present")
        else:
            print(f"node with value {value} is not present")

    def __InOrderPredecessor(self, node):
        # One step to left
        node = node.left
        
        # then right most
        while(node.right is not None):
            node = node.right
        return node 
    
    def __InOrderSuccessor(self, node):
        # One step to right
        node = node.right
        
        # then left most
        while(node.left is not None):
            node = node.left
        return node 
    
    def __delete(self, node, value):
        #case 1 and 2
        if (node is None):
            return node 
        elif (node.data > value):
            node.left = self.__delete(node.left, value)
        elif (node.data < value):
            node.right = self.__delete(node.right, value)
        else: #equals
            if (node.left is None):
                return node.right
            elif (node.right is None):
                return node.left
            else:
                # going here with inorder successor
                inOrderSuccessor = self.__InOrderSuccessor(node)
                self.__delete(node, inOrderSuccessor.data) # some people prefer to change the val only instead of delete the mid node.
                inOrderSuccessor.left = node.left
                inOrderSuccessor.right = node.right
                return inOrderSuccessor
        return node
     
    def deletenode(self, value):
        self.root = self.__delete(self.root, value)

bst = BST(20)
bst.insertNode(30)
bst.insertNode(18)
bst.insertNode(12)
bst.insertNode(15)
bst.insertNode(40)

bst.printInOrder()
bst.lookupNode(18)
bst.lookupNode(181)


bst2 = BST(10)
bst2.insertNode(8)
bst2.insertNode(6)
bst2.insertNode(9)
bst2.insertNode(32)
bst2.insertNode(25)
bst2.insertNode(40)
bst2.insertNode(20)
bst2.insertNode(35)
bst2.insertNode(50)

bst2.printInOrder()
# bst2.deletenode(20)
# bst2.deletenode(9)

bst2.deletenode(25)

bst2.deletenode(8)

bst2.printInOrder()