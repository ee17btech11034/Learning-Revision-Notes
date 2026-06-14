'''
Source ka array banate hai jo ki har ek ek linkedlist or List ko point krta hai . List contains Nodes which we can go to from src node (directly). 
Either we can use 2D list of list to store the [dest, weight] OR we can use Linkedlist [dest, weight, next].

For src, des we can use dict (map in Java)


If it is dense Graph then it uses more memory, better to use Matrix rep.
'''

class Graph:
    def __init__(self):
        # self.size = vertex  # we can increase the vertexes on run time, so we do not need this
        self.adjList = {}  #  self.adj_list = defaultdict(list) # -> better if we use default but here only for practice we are using this
    
    def __add_vertex(self, vertex):
        if vertex not in self.adjList:
            self.adjList[vertex] = []
    
    def add_edge(self, src, dest, isDirected=False, weight=1):
        if src not in self.adjList:
            self.__add_vertex(src)
        # temp = self.adjList[src]
        # temp.append([dest, weight])
        # self.adjList[src] = temp.copy()
        self.adjList[src].append([dest, weight])

        if (not isDirected):
            if dest not in self.adjList:
                self.__add_vertex(dest)
            self.adjList[dest].append([src, weight])
    
    def printGraph(self):
        for key, value in self.adjList.items():
            print(key, value)



# This line checks if the file is being run DIRECTLY, or being imported
if __name__ == "__main__":
    G1 = Graph()
    G1.add_edge(1, 2)
    G1.add_edge(1, 4)
    G1.add_edge(2, 4)
    G1.add_edge(2, 3)
    G1.add_edge(4, 3)
    G1.add_edge(5, 3)
    G1.add_edge(5, 4)

    G1.printGraph()
