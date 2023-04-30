import networkx as nx
#Create an example graph with a set of 6 nodes
G = nx.Graph()
G.add_node_from(['A', 'B', 'C', 'D', 'E', 'F'])
#Add seams between nodes with weights
G.add_edge('A', 'B', weight = 4)
G.add_edge('A', 'C', weight = 3)
G.add_edge('B', 'C', weight = 1)
G.add_edge('B', 'D', weight = 2)
G.add_edge('C', 'D', weight = 5)
G.add_edge('C', 'E', weight = 6)
G.add_edge('D', 'E', weight = 7)
G.add_edge('D', 'F', weight = 4)
G.add_edge('E', 'F', weight = 5)
#Calculate the smallest spanning tree
T = nx.minimum_spanning_tree(G)
#Print result
print(sorted(T.edges(data=True)))