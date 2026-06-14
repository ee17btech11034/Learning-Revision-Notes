'''
Graph can be represented in 2 ways:=> 1. Matrix representation, 2. Adjacency list representation

with "Undirected, directed, weighted graphs".
'''

############ Matrix Prepresentation ################
'''
v*v ki mat. 


Easy to write but wastage of memory as we are storing 0 val as well.

When no of edges are higher then it is called "Dense Graph"
When no of edges are less then it is called "Sparse Graph"
'''
class Graph:
    def __init__(self, vertex):
        self.size = vertex
        self.mat = [[0]*vertex for _ in range(vertex)]
    
    def add_edge(self, src, dest, isDirected=False, weight=1):
        '''It will cover all types of Graph'''
        # check if src and dest are in range, like no out of range val given.
        if ((0 <= src < self.size) and (0 <= dest < self.size)):
            self.mat[src][dest] = weight
            if (not isDirected):
                self.mat[dest][src] = weight
        else:
            print("Invalid Edge.")

    def printGraph(self):
        '''Print Mat rep of Graph'''
        # generally we need to run 2 loops to print all elements but Python has other functionality as well.

        for row in self.mat:
            # print(row) # this can also do the job but we can do something as well.

            # convert in str and then print
            print(' '.join(map(str, row)))
            
G1 = Graph(5)
G1.add_edge(0, 1)
G1.add_edge(0, 2)
G1.add_edge(1, 3)
G1.add_edge(2, 3)
G1.add_edge(2, 4)
G1.add_edge(3, 4)

G1.printGraph()