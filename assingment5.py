
# q1
def calculate_fitness(chromosome):
    tw = 0
    tp = 0
    for x in range(len(chromosome)):
        if chromosome[x] == 1:
            tw += weight[x]
            tp += profit[x]
    return tw, tp


def crossover():
    crossover_point = int(n / 2)
    c1 = parent1[:crossover_point] + parent2[crossover_point:]
    c2 = parent2[:crossover_point] + parent1[crossover_point:]
    return c1, c2


def mutate(chromosome):
    mutation_point = k
    if chromosome[mutation_point] == 0:
        chromosome[mutation_point] = 1
    else:
        chromosome[mutation_point] = 0
    return chromosome


def sort_pop():
    result = []
    for chromosome in population:
        cw, cp = calculate_fitness(chromosome)
        if cw <= max_weight:
            result.append([cp, chromosome])
    result = sorted(result, reverse=True)
    r = []
    for z in result:
        if z[1] not in r:
            r.append(z[1])
    return r


# Main
weight = [45, 40, 50, 90]
profit = [3, 5, 8, 10]

print("Weight", weight)
print("Profit", profit)

max_weight = 100
n = 4
population = [[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1]]
generations = 10
print(population)
k = 3
for i in range(generations):
    population = sort_pop()
    print(population)
    parent1 = population[-2]
    parent2 = population[-1]

    child1, child2 = crossover()

    child1 = mutate(child1)
    k = k - 1
    if k == -1:
        k = 3

    population.append(child1)
    population.append(child2)

population = sort_pop()
w, p = calculate_fitness(population[0])
print("\nThe best solution:")
print(population[0])
print("Weight:", w)
print("Value:", p)

# q2
def calculate_fitness(chromosome):
    tw = 0
    tp = 0
    for x in range(len(chromosome)):
        if chromosome[x] == 1:
            tw += weight[x]
            tp += profit[x]
    return tw, tp


def crossover():
    crossover_point = int(n / 2)
    c1 = parent1[:crossover_point] + parent2[crossover_point:]
    c2 = parent2[:crossover_point] + parent1[crossover_point:]
    return c1, c2


def mutate(chromosome):
    mutation_point = mp[k]
    if chromosome[mutation_point] == 0:
        chromosome[mutation_point] = 1
    else:
        chromosome[mutation_point] = 0
    return chromosome


def sort_pop():
    result = []
    for chromosome in population:
        cw, cp = calculate_fitness(chromosome)
        if cw <= max_weight:
            result.append([cp, chromosome])
    result = sorted(result, reverse=True)
    r = []
    for z in result:
        if z[1] not in r:
            r.append(z[1])
    return r


# Main
weight = [2, 3, 4, 5]
profit = [3, 5, 7, 9]

print("Weight", weight)
print("Profit", profit)

max_weight = 9
n = 4
population = [[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1]]
generations = 10
print(population)
mp = [2, 0, 3, 1]
k = 0
for i in range(generations):
    population = sort_pop()
    print(population)
    parent1 = population[-1]
    parent2 = population[-2]

    child1, child2 = crossover()

    child1 = mutate(child1)
    k = k + 1
    if k == 4:
        k = 0

    population.append(child1)
    population.append(child2)

population = sort_pop()
w, p = calculate_fitness(population[0])
print("\nThe best solution:")
print(population[0])
print("Weight:", w)
print("Value:", p)

# q3

import math
import random


def heuristic(sol):
    h1 = 0
    a, b, c, d = sol
    f = [[not a or d], [c or b], [not c or not d], [not d or not b], [not a or not d]]
    for i in f:
        if i[0]:
            h1 = h1 + 1
    return h1


def generate_new(sol):
    index = random.randint(0, 3)
    if sol[index] == 1:
        sol[index] = 0
    else:
        sol[index] = 1
    return sol


initial = [1, 1, 1, 1]
t = 500
s = initial
ho = heuristic(s)
k = 0
print(s, ho)
while t > 0:
    s1 = generate_new(s)
    hn = heuristic(s1)
    e = hn - ho
    if hn > ho:
        s = s1
    else:
        p = 1/(1 + math.e**(-e/t))
        if p >= 0.5:
            s = s1
    print(s1, hn)
    ho = hn
    t = t - 50
