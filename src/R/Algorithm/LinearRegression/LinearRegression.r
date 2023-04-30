#Create Database
x1 <- c(1, 2, 3, 4, 5)
x2 <- c(2, 4, 5, 4, 5)
y <- c(3, 6, 7, 7, 8)
#Create input matrix
X <- matrix(c(rep(1, 5), x1, x2), ncol = 3)
#Calculate the product of the matrices to give a linear regression model
beta <- solve(t(X) %*% X) %*% t(X) %*% y
#Show beta coefficient results
beta