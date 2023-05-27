from collections import deque

class Graph:
 
    def __init__(self):
        self.graph = {}
        self.start = None
 
    def addEdge(self, u, v):
        if not self.graph:
            self.start = u
            self.graph[u]=[v]
        else:
            self.graph[u]=self.graph.get(u, [])+[v]

    def count_lvl_nodes(self, lvl_):
        if not self.graph:
            return 0
        visited=set()
        q = deque()
        q.append(self.start)
        visited.add(self.start)
        
        lvl=0
        while q:
            lvl+=1
            for _ in range(len(q)):
                el=q.popleft()
                if lvl==lvl_:
                    print(el)
                if self.graph.get(el):
                    for adj in self.graph[el]:
                        if adj not in visited:
                            visited.add(adj)
                            q.append(adj)
        
    
g = Graph()
g.addEdge(0, 3)
g.addEdge(0, 2)
g.addEdge(0, 1)
g.addEdge(2, 1)
g.addEdge(2, 4)
g.addEdge(3, 1)
g.addEdge(3, 2)

print(g.graph)

level=2
g.count_lvl_nodes(level)