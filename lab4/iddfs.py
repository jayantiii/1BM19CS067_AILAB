from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u: int, v: int):
        self.graph[u].append(v)

    def DLS(self, src: int, target: int, limit: int):

        if(src == target):
            return True

        if(limit <= 0):
            return False

        for i in self.graph[src]:
            if(self.DLS(i, target, limit-1)):
                return True

        return False

    def IDDFS(self, src: int, target: int, limit: int):
        for i in range(limit):
            if(self.DLS(src, target, i)):
                return True
        return False
### Enter endges in the format <{u} {v}> where u is the starting vertice, and v is the ending vertice
k = int(input("Enter the number of edges: "))
g = Graph(k)
print(f'Enter {k} edges')
for i in range((k)):
    u, v = input(f'Edge {i} u and v: ').split()
    g.addEdge(int(u), int(v))
Enter 6 edges
while(True):
    target, maxDepth, src = input(
        "Enter the Target, maxDepth & src \n").split()
    if g.IDDFS(int(src), int(target), int(maxDepth)) == True:
        print("Target is reachable from source " +
              "within max depth")
    else:
        print("Target is NOT reachable from source " +
              "within max depth")

    cont = input("Test another vertice? (y / n) ")
    if cont in ['n', 'N']:
        break
