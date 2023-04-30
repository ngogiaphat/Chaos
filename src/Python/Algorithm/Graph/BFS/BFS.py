from queue import Queue
#Create a Graph
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
def bfs_shortest_path(graph, start, end):
    #Create the first values
    q = Queue()
    visited = []
    path = {}
    #Start searching for the shortest path
    q.put(start)
    visited.append(start)
    #If the target vertex is found, stop the search
    while not q.empty():
        current_node = q.get()
        if current_node == end:
            break
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                q.put(neighbor)
                visited.append(neighbor)
                path[neighbor] = current_node
    #Create a path from a vertex to any vertex
    shortest_path = [end]
    while end != start:
        shortest_path.append(path[end])
        end = path[end]
    shortest_path.reverse()
    return shortest_path
#Use bfs_shortest_path function to find the shortest path from vertex A to F in graph
print(bfs_shortest_path(graph, 'A', 'F'))