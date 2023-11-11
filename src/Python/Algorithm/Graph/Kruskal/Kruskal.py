graph = {
    'A': {
        'B': 6,
        'D': 1,
    },
    'B': {
        'A': 6,
        'C': 5,
        'D': 2,
    },
    'C': {
        'B': 5,
        'E': 1,
    },
    'D': {
        'A': 1,
        'B': 2,
        'C': 5,
        'E': 1,
    },
    'E': {
        'C': 1,
        'D': 1,
    }
}
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1
def kruskal(graph):
    result = []
    i = 0
    e = 0
    parent = {}
    rank = {}
    for node in graph:
        parent[node] = node
        rank[node] = 0
    edges = sorted(
        [(graph[node][neighbor], node, neighbor) for node in graph for neighbor in graph[node]], reverse = True)
    while e < len(graph) - 1:
        w, u, v = edges[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e = e + 1
            result.append([u, v, w])
            union(parent, rank, x, y)
    return result
print(kruskal(graph))