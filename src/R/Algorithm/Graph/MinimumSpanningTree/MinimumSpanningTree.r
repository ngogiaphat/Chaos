#Create the adjacency matrix of the graph
adj_mtx <- matrix(c(0, 4, Inf, Inf, Inf, Inf, 8, 0, 8, Inf, Inf, Inf, Inf, 8, 0, 7, Inf, Inf, Inf, Inf, 7, 0, 9, 14, Inf, Inf, Inf, Inf, 4, 0, 10, Inf, 2, Inf, Inf, 8, 10, 0, 11, Inf, Inf, 7, Inf, Inf, 11, 0, Inf, Inf, Inf, 2, Inf, Inf, Inf, 9, 14, Inf, Inf, 0), ncol = 9, byrow = TRUE)
#Find Minimum Spanning Tree by Prim Algorithm 
tree <- matrix(nrow = nrow(adj_mtx)-1, ncol = 2)
row_names <- row.names(adj_mtx)
#Select the first vertex as the starting vertex
v <- row_names[1] 
for (i in 1:(nrow(adj_mtx)-1)) {
  min_edge_weight <- Inf
  min_edge_v <- v
  for (j in 1:length(row_names)) {
    if (row_names[j] %in% v) {
      next
    } 
    else {
      edges <- adj_mtx[row.names == v, row.names == row_names[j]]
      edge_weight <- as.numeric(edges)
      if (edge_weight < min_edge_weight) {
        min_edge_weight <- edge_weight
        min_edge_v <- row_names[j]
      }
    }
  }
  tree[i,] <- c(v, min_edge_v)
  v <- c(v, min_edge_v)
}
#Print Minimum Spanning Tree
cat("Minimum spanning tree: \n")
for (i in 1:nrow(tree)) {
  cat(tree[i,1], "-", tree[i,2], "\n")
}




#Solution:




#First, we create the adj_mtx adjacency matrix of the graph with the edges between vertices filled in, where Inf is used to represent the infinity distance between non-connected vertices.
#Next, we find the spanning tree of the graph using Prim's algorithm. 
#We start by selecting the first vertex in row_names as the starting vertex, then traverse the edges of that vertex to find the least weighted edge that connects to an unselected vertex. 
#We take that vertex and that edge into the spanning tree, then repeat the process until we find n-1 edges (where n is the total number of vertices in the graph).
#Finally, we print the edges in the spanning tree.