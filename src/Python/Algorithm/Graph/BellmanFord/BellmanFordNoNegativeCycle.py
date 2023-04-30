graph = {
    'A': {'B': 6, 'D': 1},
    'B': {'C': 5, 'D': 2},
    'C': {'E': 1},
    'D': {'B': -2, 'C': -4, 'E': 1},
    'E': {}
}
def bellman_ford(graph, start):
    dist = {vertex: float('inf') for vertex in graph}
    dist[start] = 0
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor in graph[node]:
                new_dist = dist[node] + graph[node][neighbor]
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
    return dist
print(bellman_ford(graph, 'A'))