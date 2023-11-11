import math
# Initialization of parent matrix suppose max range of a node is up to 1000 if there are 1000 nodes than also length of jump matrix will not exceed 10
jump = [
    [0 for j in range(10)]
	for i in range(1000)
]
# Node array is used to store all nodes
node = [0 for i in range(1000)]
# isNode is an array to check whether
# a node is present in graph or not
isNode = [0 for i in range(1000)]
# n -> it represent total number of nodes
# len -> it is the maximum length of array to hold parent of each node. In worst case, the highest value of parent a node can have is n-1.
# 2 ^ len <= n-1
# len = O(log2n)
def getLen(n):
	len = int((math.log(n)) // (math.log(2))) + 1
	return len
# jump represent 2D matrix to hold parent of node in jump matrix here we pass reference of 2D matrix so that the
# change made occur directly to the original matrix len is same as defined above n is total nodes in graph
def set_jump_pointer(len, n):
	global jump, node
	for j in range(1,len + 1):
		for i in range(0, n):
			jump[node[i]][j] = jump[jump[node[i]][j - 1]][j - 1]
# c -> it represent child
# p -> it represent parent
# i -> it represent node number
# p=0 means the node is root node
# here also we pass reference of
# 2D matrix and depth vector so
# that the change made occur
# directly to the original matrix
# and original vector
def constructGraph(c, p, i):
	global jump, node, isNode
	# Enter the node in node array it stores all the nodes in the graph
	node[i] = c
	# To confirm that no child node have 2 parents
	if (isNode == 0):
		isNode = 1
		# Make parent of x as y
		jump[0] = p
	return
# function to jump to Lth parent
# of any node
def jumpPointer(x, L):
	j = 0
	n = x
	k = L
	global jump, isNode
	# To check if node is present in graph or not
	if (isNode[x] == 0):
		print("Node is not present in graph ")
		return
	# In this loop we decrease the value of L by L/2 and increment j by 1 after each iteration and check for set bit if we get set bit
	# then we update x with jth parent of x as L becomes less than or equal to zero means we have jumped to Lth parent of node x
	while (L > 0):
		# To check if last bit is 1 or not
		if ((L & 1)!=0):
			x = jump[x][j]
		# Use of shift operator to make
		# L = L/2 after every iteration
		L = L >> 1
		j += 1
	print(str(k) + "th parent of node " + str(n) + " is = " + str(x))
	return
# Driver code
if __name__=="__main__":
	# n represent number of nodes
	n = 11
	# Function to calculate len len -> it is the maximum length of array to hold parent of each node.
	len = getLen(n)
	# R stores root node
	R = 2
	# Construction of graph here 0 represent that the node is root node
	constructGraph(2, 0, 0)
	constructGraph(5, 2, 1)
	constructGraph(3, 5, 2)
	constructGraph(4, 5, 3)
	constructGraph(1, 5, 4)
	constructGraph(7, 1, 5)
	constructGraph(9, 1, 6)
	constructGraph(10, 9, 7)
	constructGraph(11, 10, 8)
	constructGraph(6, 10, 9)
	constructGraph(8, 10, 10)
	# Function to pre compute jump matrix
	set_jump_pointer(len, n)
	# Query to jump to parent using jump pointers query to jump to 1st parent of node 2
	jumpPointer(2, 0)
	# Query to jump to 2nd parent of node 4
	jumpPointer(4, 2)
	# Query to jump to 3rd parent of node 8
	jumpPointer(8, 3)
	# Query to jump to 5th parent of node 20
	jumpPointer(20, 5)
# This code is contributed by rutvik_56