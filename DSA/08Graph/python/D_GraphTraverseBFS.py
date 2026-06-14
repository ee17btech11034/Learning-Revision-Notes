"""
BFS:
    1. Using Queue:

"""

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
    
    def bfsUsingQueue(self, startnode=1):
        '''Here we will be using queue to do BFS'''
        # visited = [False]*(self.size)
        visited = [False]*(self.size +1) # if 1 based node start

        queue = []
        ans = []
        temp = []

        queue.append(startnode)
        queue.append(None)

        while(len(queue) > 1):
            node = queue.pop(0)
            if (node):
                visited[node] = True
                temp.append(node)
                for connectedNode in self.adjlist[node]:
                    if (not visited[connectedNode]):
                        queue.append(connectedNode)
                        # visited[connectedNode] = True
            else:
                queue.append(None) # None shows that it is the level complete
                ans.append(temp.copy())
                temp = []
        
        if (temp):
            ans.append(temp.copy())
        print("Level Order Traversal (BFS):", end=" ")
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
    G1.bfsUsingQueue()