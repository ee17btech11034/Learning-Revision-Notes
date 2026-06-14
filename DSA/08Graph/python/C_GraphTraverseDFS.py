"""
DFS:
    1. Using STack:
    2. Using recursion

MST (Minimum Spanning Tree):
    - # when we use visited array, then if we remove unvisited edges then it will look like tree, that is called "Minimum Spanning Tree (MST)". 
"""
'''
from B_GraphAdjacencyListRepresentation import Graph

if __name__=="__main__":
    g2 = Graph()
    g2.add_edge(1, 2)
    g2.add_edge(1, 3)
    g2.add_edge(2, 3)
    g2.add_edge(4, 3)
    g2.add_edge(5, 3)
    g2.add_edge(5, 6)
    g2.add_edge(4, 6)
    g2.printGraph()

'''

from collections import defaultdict

class Graph:
    def __init__(self, vertex):
        self.adjlist = defaultdict(list)
        self.size = vertex
    
    def add_edge(self, src, dest):
        self.adjlist[src].append(dest)
        self.adjlist[dest].append(src)
    
    def printGraph(self):
        for key, val in self.adjlist.items():
            print(key, " -> ", val)
    
    def dfsUsingStack(self, startnode=1):
        '''Here we will be using stack to do DFS'''
        # visited = [False]*(self.size)
        visited = [False]*(self.size +1) # if 1 based node start

        stack = []
        ans = []

        # take the start node
        stack.append(startnode) # added in stack
        visited[startnode] = True

        while(stack):
            # node = stack[-1] # top element pick and fid all relation nodes & visit
            node = stack.pop()
            ans.append(node) # either we can print here or can store that in ans and then later can print
            for connectednode in self.adjlist[node]:
                if (not visited[connectednode]):
                    stack.append(connectednode)
                    visited[connectednode] = True

        # if graph is disconnected
        # for i in range(1, self.size+1):
            # again call dfsstack method or again write the code or wrap whole above code in this. 
        
        print("MST/dfsUsingStack:", end=" ")
        # when we use visited array, then if we remove unvisited edges then it will look like tree, thatis called "Minimum Spanning Tree (MST)". 
        for node in ans:
            print(node, end=" ")
        print()

    def __dfsRecursion(self, node, visited, ans):
        ans.append(node)
        visited[node] = True
        for connectedNode in self.adjlist[node]:
            if (not visited[connectedNode]):
                visited[connectedNode] = True
                self.__dfsRecursion(connectedNode, visited, ans)
    
    def dfsUsingRecursion(self, startnode=1):
        ans = []
        visited = [False]*(self.size +1)
        self.__dfsRecursion(startnode, visited, ans)

        print("MST/dfsUsingRecursion:", end=" ")
        # when we use visited array, then if we remove unvisited edges then it will look like tree, thatis called "Minimum Spanning Tree (MST)". 
        for node in ans:
            print(node, end=" ")
        print()

if __name__ == "__main__":
    G1 = Graph(5)
    G1.add_edge(1, 2)
    G1.add_edge(1, 4)
    G1.add_edge(2, 4)
    G1.add_edge(2, 3)
    G1.add_edge(4, 3)
    G1.add_edge(5, 3)
    G1.add_edge(5, 4)

    G1.printGraph()
    G1.dfsUsingStack()
    G1.dfsUsingRecursion()