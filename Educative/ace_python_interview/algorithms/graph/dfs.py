class Graph:
 
    # Constructor
    def __init__(self):
        self.graph = {}
        self.start = None
 
    def addEdge(self, u, v):
        if not self.graph:
            self.start = u
            self.graph[u]=[v]
        else:
            self.graph[u]=self.graph.get(u, [])+[v]

    def DFS(self):
        if not self.graph:
            return 0
        visited=set()
        s=[]
        s.append(self.start)
        visited.add(self.start)
        
        while s:
            el=s.pop()
            print(el)
            if self.graph.get(el):
                for adj in self.graph[el]:
                    if adj not in visited:
                        visited.add(adj)
                        s.append(adj)
                        print(s)
        
    
g = Graph()
g.addEdge(0, 3)
g.addEdge(0, 2)
g.addEdge(0, 1)
g.addEdge(2, 4)
g.addEdge(2, 3)
g.addEdge(3, 2)
print(g.graph)
g.DFS()