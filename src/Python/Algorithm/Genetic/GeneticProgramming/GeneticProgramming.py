import random
def generate_individual(length):
    return [random.choice(["+", "-", "*", "/"]) if i%2 else random.randint(0, 10) for i in range(length)]
def calculate_fitness(individual):
    try:
        eval("".join(str(i) for i in individual))
    except ZeroDivisionError:
        return 0
    target = 1000
    return 1/(abs(eval("".join(str(i) for i in individual)) - target) + 0.001)
def mutate(individual):
    mutation_point = random.randint(0, len(individual)-1)
    if mutation_point % 2 == 0:
        individual[mutation_point] = random.randint(0, 10)
    else:
        individual[mutation_point] = random.choice(["+", "-", "*", "/"])
    return individual
def crossover(parent1, parent2):
    mid_point = random.randint(1, len(parent1)-1)
    return parent1[:mid_point] + parent2[mid_point:]
def create_next_generation(current_generation):
    generation_size = len(current_generation)
    sort_by_fitness = sorted(current_generation, key = calculate_fitness, reverse=True)
    next_generation = sort_by_fitness[:int(generation_size/2)]
    while len(next_generation) < generation_size:
        parent1 = random.choice(sort_by_fitness)
        parent2 = random.choice(sort_by_fitness)
        next_generation.append(crossover(parent1, parent2))
    next_generation = [mutate(i) if random.random() < 0.2 else i for i in next_generation]
    return next_generation
population_size = 100
generation_size = 500
generation = [generate_individual(5) for _ in range(population_size)]
for i in range(generation_size):
    generation = create_next_generation(generation)
best_individual = max(generation, key = calculate_fitness)
print(best_individual)
print(eval("".join(str(i) for i in best_individual)))