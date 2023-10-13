g <- graph(edges = c(1,2,1,3,2,3,2,4,3,4,3,5,4,5,5,6), n = 6, directed = F)
#Use Bellman - Ford algorithm to calculate the shortest path
result <- bellman.ford(g, v = 1, to = 6)
#Print the shortest path and its length
if(result$negative_cycle == TRUE){
  message("Đồ thị có chu trình âm")
}
else if(result$dist[6] == Inf){
  message("Không có đường đi từ đỉnh 1 đến đỉnh 6")
}
else {
  #Print the shortest path
  path <- get.shortest.paths(g, from = 1, to = 6, output = "epath")[[1]]$epath
  message("Đường đi ngắn nhất:", path)
  #Print the length of the shortest path
  message("Độ dài của đường đi ngắn nhất:", result$dist[6])
}