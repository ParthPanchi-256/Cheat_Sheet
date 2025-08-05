import math

# Depth First Search
def dfs(node, graph, ancestor, parent):
    ancestor[node][0] = parent
    for neighbor in graph[node]:
        dfs(neighbor, graph, ancestor, node)

# Method to initialize ancestor table
def preprocess(graph, ancestor, V, maxN):
    dfs(1, graph, ancestor, -1)
    for j in range(1, maxN):
        for i in range(1, V + 1):
            if ancestor[i][j - 1] != -1:
                ancestor[i][j] = ancestor[ancestor[i][j - 1]][j - 1]

# Method to find Kth ancestor of node
def find_kth_ancestor(ancestor, node, K, maxN):
    for i in range(maxN - 1, -1, -1):
        if K & (1 << i):
            if ancestor[node][i] == -1:
                return -1
            node = ancestor[node][i]
    return node

if __name__ == "__main__":
    V = 7
    maxN = int(math.log2(V)) + 1

    # edge list
    edges = [[1, 2], [1, 3], [3, 4], [4, 5], [4, 6], [5, 7]]
    graph = [[] for _ in range(V + 1)]
    ancestor = [[-1] * maxN for _ in range(V + 1)]

    # construct the adjacency list
    for edge in edges:
        graph[edge[0]].append(edge[1])

    # preprocessing
    preprocess(graph, ancestor, V, maxN)

    # queries
    print(find_kth_ancestor(ancestor, 7, 3, maxN))
    print(find_kth_ancestor(ancestor, 5, 1, maxN))
    print(find_kth_ancestor(ancestor, 7, 4, maxN))
    print(find_kth_ancestor(ancestor, 6, 4, maxN))