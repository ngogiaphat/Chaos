from queue import Queue
#Create a Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
def dfs_path(graph, start, end, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = [start]
    if start == end:
        return path
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs_path(graph, neighbor, end, visited, path + [neighbor])
            if new_path is not None:
                return new_path
print(dfs_path(graph, 'A', 'F'))