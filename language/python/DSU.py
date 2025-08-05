class DSU:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1]*N

    def find(self, v):
        if (v == self.parent[v]):
            return v
        self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    def union(self,v,u):
        pv = self.find(v)
        pu = self.find(u)
        if pv == pu:
            return 
        if(self.size[pu]> self.size[pv]):
            pv,pu = pu,pv
        
        self.parent[pu] = pv
        self.size[pv]+=self.size[pu]

if __name__ == "__main__":
    N = int(input("Number of nodes:"))
    djs = DSU(N)
    
    print(djs.find(3))
    djs.union(2,3)
    print(djs.find(3), djs.find(2))

