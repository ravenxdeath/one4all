import random

def generate_initial_population(pop_size, N, T):
    initial_pop = []
    for _ in range(pop_size):
        indiv_chromosome = ''.join(random.choice('01') for _ in range(N * T))
        initial_pop.append(indiv_chromosome)
    return initial_pop

def calculate_fitness(indiv_chromosome, N, T):
    overlap_pen = 0
    consistency_pen = 0
    time_segments = [indiv_chromosome[i * N:(i + 1) * N] for i in range(T)]
    
    # Overlap penalty calculation
    for seg in time_segments:
        course_count = sum(int(bit) for bit in seg)
        if course_count > 1:
            overlap_pen += course_count - 1
    
    # Consistency penalty calculation
    course_schedule = [0] * N
    for seg in time_segments:
        for i, bit in enumerate(seg):
            course_schedule[i] += int(bit)
    
    for count in course_schedule:
        if count != 1:
            consistency_pen += abs(count - 1)
    
    fitness_value = -(overlap_pen + consistency_pen)
    return fitness_value

def select_parents(population, fitness_vals):
    total_fitness = sum(fitness_vals)
    prob_selection = [fit / total_fitness for fit in fitness_vals]
    selected_parents = random.choices(population, prob_selection, k=2)
    return selected_parents

def single_point_crossover(parent1, parent2):
    cross_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:cross_point] + parent2[cross_point:]
    child2 = parent2[:cross_point] + parent1[cross_point:]
    return child1, child2

def mutate(indiv_chromosome, mutation_prob):
    chromo_list = list(indiv_chromosome)
    for i in range(len(chromo_list)):
        if random.random() < mutation_prob:
            chromo_list[i] = '1' if chromo_list[i] == '0' else '0'
    return ''.join(chromo_list)

def genetic_algorithm(N, T, population_size=100, max_generations=1000, mutation_rate=0.01):
    population = generate_initial_population(population_size, N, T)
    optimal_chromosome = None
    optimal_fitness = float('-inf')
    
    for gen in range(max_generations):
        fitness_values = [calculate_fitness(indiv, N, T) for indiv in population]
        
        if max(fitness_values) > optimal_fitness:
            optimal_fitness = max(fitness_values)
            optimal_chromosome = population[fitness_values.index(optimal_fitness)]
        
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = select_parents(population, fitness_values)
            offspring1, offspring2 = single_point_crossover(parent1, parent2)
            offspring1 = mutate(offspring1, mutation_rate)
            offspring2 = mutate(offspring2, mutation_rate)
            new_population.extend([offspring1, offspring2])
        
        population = new_population[:population_size]
    
    return optimal_chromosome, optimal_fitness

# Example usage:
N = 3  # Number of courses
T = 3  # Number of timeslots
population_size = 100
max_generations = 1000
mutation_rate = 0.01

best_chromosome, best_fitness = genetic_algorithm(N, T, population_size, max_generations, mutation_rate)
print("Best Chromosome:", best_chromosome)
print("Best Fitness:", best_fitness)
