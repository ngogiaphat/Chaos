#Generate sample data
set.seed(123)
data <- data.frame(x = runif(50, min = 0, max = 10))
#Set the parameters for the genetic algorithm
#Population size
pop_size <- 20
#Number of generations
num_generations <- 50
#Mutation rate
mutation_rate <- 0.1
#The fitness function of the individual
fitness <- function(x, target = 5){
  return(1 / abs(x - target))
}
#Initial population constructor
initialize_population <- function(size){
  return(data.frame(x = runif(size, min = 0, max = 10)))
}
#Function to select individuals in a population
tournament_selection <- function(population, tournament_size = 3){
  #Randomly select candidates from the population
  contestants <- sample(nrow(population), size = tournament_size, replace = FALSE) # nolint: line_length_linter.
  #Sort the contestants by increasing fitness and choose the best contestant
  return(population[contestants[order(population$x[contestants])][1],])
}
#Hybrid function between 2 individuals
crossover <- function(parent1, parent2) {
  #Choose a random hybrid point
  crossover_point <- sample(1:nrow(parent1), size = 1) # nolint: line_length_linter.
  #Create a child by combining the 2 tails of 2 parents
  child <- rbind(parent1[1:crossover_point, ], parent2[(crossover_point + 1):nrow(parent2)]) # nolint: line_length_linter.
  return(data.frame(x = child))
}
#Individual mutation function
mutate <- function(individual, mutation_rate){
  #Check for mutations
  if(runif(1) < mutation_rate){
    #Increase or decrease the value of a random instance
    individual$x <- individual$x + runif(1, min = -1, max = 1)
  }
  return(individual)
}
#The function that runs the genetic algorithm
genetic_algorithm <- function(data, pop_size, num_generations, mutation_rate){
    #Create the initial population
    population <- initialize_population(pop_size)
    #Repeat for the specified number of generations
    for(generation in 1:num_generations){
        #Calculate the fitness of each individual in the population
        population$fitness <- fitness(population$x)
        #Print out the current generation and the best value in the population
        cat(paste("Generation:", generation, "Best value:", max(population$fitness), "\n")) # nolint: line_length_linter.
        # The above code implements a simple genetic algorithm to find the x value that is close to the target value of the fitness function. # nolint: line_length_linter.
        # Specifically, the algorithm will create an initial population, and then iterate for a given number of generations.  # nolint
        # In each generation, the algorithm will calculate the fitness of each individual in the population, # nolint: line_length_linter.
        # then select individuals to cross and mutate to create a new generation. # nolint: line_length_linter.
        # Then, the algorithm selects the best individuals to become the next generation's population. # nolint: line_length_linter.
        # Finally, the algorithm returns the final best fitness value.
        # In the above code, the target value of the fitness function is set to 5 # nolint: line_length_linter.
        # and other parameters of the algorithm such as population size, number of generations and mutation rate are also set. # nolint: line_length_linter.
        # Selection of individuals in a population for hybridization # nolint: line_length_linter.
        parents <- replicate(pop_size/2, {
            #Perform selection and crossover to create new children
            child1 <- crossover(select(population, fitness, tournament_size), select(population, fitness, tournament_size), crossover_rate) # nolint: line_length_linter.
            child2 <- crossover(select(population, fitness, tournament_size), select(population, fitness, tournament_size), crossover_rate) # nolint: line_length_linter.
            #Return the pair of children as a matrix
            matrix(c(child1, child2), nrow = 2)
        },
        simplify = FALSE)
    }
}