
def genetic_algorithm(pop_size, generations, lessons, teachers):
    population = initialize_population(pop_size, lessons, teachers)
    
    for generation in range(generations):
        for chromosome in population:
            chromosome.calculate_fitness()

        # Select parents
        parents = select_parents(population)
        
        # Create next generation through crossover and mutation
        next_gen = []
        while len(next_gen) < pop_size:
            parent1, parent2 = random.sample(parents, 2)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1)
            mutate(child2)
            next_gen.extend([child1, child2])

        population = next_gen

        # Optionally track and print best fitness each generation
        best = max(population, key=lambda x: x.fitness)
        print(f"Generation {generation}: Best Fitness = {best.fitness}")
    
    return max(population, key=lambda x: x.fitness)  # Return the best solution


def initialize_population(pop_size, lessons, teachers):
    population = []
    for _ in range(pop_size):
        schedule = create_random_schedule(lessons, teachers)  # Implement this function
        chromosome = Chromosome(schedule)
        population.append(chromosome)
    return population
