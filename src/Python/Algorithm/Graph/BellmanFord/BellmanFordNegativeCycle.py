INF = float('inf')
def BellmanFord(graph, V, src):
    dist = [INF] * V
    dist[src] = 0
    for _ in range(V - 1):
        for u, v, weight in graph:
            if dist[u] != INF and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
    for u, v, weight in graph:
        if dist[u] != INF and dist[u] + weight < dist[v]:
            return "Đồ thị có chu trình âm"
    return dist

def findMinSpanningTree(graph, V):
    src = 0
    dist = BellmanFord(graph, V, src)
    if dist == "Đồ thị có chu trình âm":
        return "Không có cây khung nhỏ nhất"
    min_span_tree = []
    visited = [False] * V
    pq = [(0, -1, src)]
    while len(pq) > 0:
        cost, prev, node = heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        if prev != -1:
            min_span_tree.append((prev, node, cost))
        for adj_node, weight in adj_list[node]:
            if not visited[adj_node]:
                heappush(pq, (weight, node, adj_node))
    return min_span_tree