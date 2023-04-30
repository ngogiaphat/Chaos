import random
"""Define the function to be optimized"""
def fitness_function(x):
    return -x**2 + 5

"""Initial population initialization"""    
def generate_population(size, chromosome_length):
    population = []
    for i in range(size):
        chromosome = []
        for j in range(chromosome_length):
            chromosome.append(random.randint(0, 1))
        population.append(chromosome)
    return population

"""The value of each individual in the population"""
def calculate_fitness(population):
    fitness_scores = []
    for chromosome in population:
        x = int ("".join(str(gene) for gene in chromosome), 2)
        fitness_scores.append(fitness_function(x))
    return fitness_scores

"""Select 2 parents for hybridization"""
def select_parents(population, fitness_scores):
    total_fitness = sum(fitness_scores)
    parent1_probability = random.uniform(0, 1)
    parent2_probability = random.uniform(0, 1)
    parent1 = None
    parent2 = None
    fitness_sum = 0
    for i in range(len(fitness_scores)):
        fitness_sum += fitness_scores[i]
        if fitness_sum / total_fitness >= parent1_probability and not parent1:
            parent1 = population[i]
        if fitness_sum / total_fitness >= parent2_probability and not parent2:
            parent2 = population[i]
        if parent1 and parent2:
            break
    return parent1, parent2

"""Crossing between two parents to create offspring"""
def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

"""Mutation an individual with a mutation rate of mutation_rate"""
def mutate(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.uniform(0, 1) < mutation_rate:
            chromosome[i] = 1 - chromosome[i]
    return chromosome

"""Apply Genetic Algorithm to optimize the function"""
def genetic_algorithm(population_size, chromosome_length, mutation_rate, generations):
    population = generate_population(population_size, chromosome_length)
    best_fitness = -float("inf")
    best_individual = None
    for generation in range(generations):
        fitness_scores = calculate_fitness(population)
        parent1, parent2 = select_parents(population, fitness_scores)
        child1, child2 = crossover(parent1, parent2)
        child1 = mutate(child1, mutation_rate)
        child2 = mutate(child2, mutation_rate)
        population.append(child1)
        population.append(child2)
        population = sorted(population, key = lambda x: fitness_function(int("".join(str(bit) for bit in x), 2)), reverse = True)
        population = population[:population_size]
        best_individual = population[0]
        best_fitness = fitness_function(int("".join(str(bit) for bit in best_individual), 2))
        print("Generation:", generation)
        print("Best individual:", best_individual)
        print("Best fitness:", best_fitness)
    return best_individual
population_size = 20
chromosome_length = 6
mutation_rate = 0.1
generations = 50
best_individual = genetic_algorithm(population_size, chromosome_length, mutation_rate, generations)