install.packages("igraph")
library(igraph)
g <- graph(edges = c(1,2,1,3,2,3,2,4,3,4,3,5,4,5,5,6), n=6, directed = FALSE)
shortest_path(g, from = 1, to = 6, algo = "breadthfirst", output="epath")