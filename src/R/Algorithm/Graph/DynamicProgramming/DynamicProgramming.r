#Create the adjacency matrix of the graph
adj_mtx <- matrix(c(0, 2, 5, Inf, Inf, Inf, Inf, 0, 7, 1, 9, Inf, Inf, Inf, 0, 4, Inf, Inf, Inf, Inf, Inf, 0, 3, 2, Inf, Inf, Inf, Inf, 0, 6, Inf, Inf, Inf, Inf, Inf, 0), ncol = 6, byrow = TRUE)
#Find the shortest path using dynamic programming algorithm
d <- rep(Inf, ncol(adj_mtx))
d[1] <- 0
for (i in 2:ncol(adj_mtx)) {
  for (j in 1:(i-1)) {
    if (adj_mtx[j,i] != Inf && d[j] + adj_mtx[j,i] < d[i]) {
      d[i] <- d[j] + adj_mtx[j,i]
    }
  }
}
#Print the shortest path from vertex 1 to other vertices
cat("Shortest paths from vertex 1:", "\n")
for (i in 2:ncol(adj_mtx)) {
  cat("Vertex", i, "-", ifelse(d[i] == Inf, "No path", d[i]), "\n")
}




#Solution: 




#We create the adj_mtx adjacency matrix of the graph with the distances between the vertices filled in. 
#Where Inf is used to represent the infinity distance between non-connected vertices.
#Next, we find the shortest path from vertex 1 to other vertices in the graph. 
#We start by letting the distance d from vertex 1 to all other vertices be infinity (Inf) except vertex 1 whose distance to it is 0. 
#Then, for each vertex i (from vertex 2 to the last vertex), we traverse vertices j (from first vertex to vertex before vertex i) to check if there is a shorter path from vertex 1 to vertex i through vertex j. 
#If so, we update the distance d from vertex 1 to vertex i. 
#Finally, we print the shortest path from vertex 1 to other vertices.