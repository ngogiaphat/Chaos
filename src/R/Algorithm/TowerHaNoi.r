move_disk <- function(disk_num, from_rod, to_rod){
  cat(paste0("Move disk ", disk_num, " from ", from_rod, " to ", to_rod, "\n"))
}
hanoi_tower <- function(disk_num, from_rod, to_rod, aux_rod){
  if(disk_num == 1){
    move_disk(disk_num, from_rod, to_rod)
    return()
  }
  hanoi_tower(disk_num - 1, from_rod, aux_rod, to_rod)
  move_disk(disk_num, from_rod, to_rod)
  hanoi_tower(disk_num - 1, aux_rod, to_rod, from_rod)
}
# Settings name of rods and number of disks
n <- 3
A <- "A"
B <- "B"
C <- "C"
# Call function
hanoi_tower(n, A, C, B)
