#Calculate and print the value of Pi with 10 digits after the decimal point
options(digits = 10)
pi
#Calculate the approximate value of Pi using Leibniz's formula
n <- 1000000
approx_pi <- 0
for(i in 0:n){
  approx_pi <- approx_pi + (-1)^i / (2*i+1)
}
approx_pi <- 4 * approx_pi
approx_pi
#Calculate the error between the estimated value and the exact value of Pi
exact_pi <- pi
error <- abs(approx_pi - exact_pi)
error