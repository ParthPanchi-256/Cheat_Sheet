
class Graph:
    def __init__(self,N,E,directed=False):
        self.adj = [[] for _ in range(N+1)]
        self.directed = directed
        for v,u in E:
            self.adj[v].append(u)
            if directed:
                self.adj[u].append(v)
        
    def addEdj(self,v,u):
        self.adj[v].append(u)
        if self.directed:
            self.adj[u].append(v)
    
    def display_adj_list(self):
        for i, arr in enumerate(self.adj):
            print(i," ->"," ".join(arr))
    
    def bfs(self,src,adj):

        

