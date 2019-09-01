#!/usr/bin/env python
# coding: utf-8

# In[3]:


import string
import random
import argparse


# In[313]:

parser = argparse.ArgumentParser()
parser.add_argument('--target', '-t', help='Target string to be generated, Default=\'to be or not to be\'',
                    default='to be or not to be', type=str)
parser.add_argument('--mutation', '-m', help='Mutation Rate, Default=0.01 (1% mutation)',
                    default=0.01, type=float)
parser.add_argument('--population', '-p', help='Population Size, Default=700 (Increase population size for longer sentences)',
                    default=700, type=int)

args = parser.parse_args()


def random_word_generator(length_of_word):
    word = ''
    i = 0
    char_list = []
    for j in range(32, 127):
        char_list.append(chr(j))
    
    while i < length_of_word:
        word = word + random.choice(char_list)
        #word = word + random.choice(string.ascii_lowercase + string.whitespace)
        i += 1
    return word


# In[288]:


def population(size):
    pop = []
    for i in range(size):
        pop.append(random_word_generator(len(target)))
    return pop


# In[329]:


def fitness(target, word):
    score = 0
    for j in range(len(word)):
        if word[j] in target:
            if word[j] == target[j]:
                score += 1
    fitness = score/len(target)
        #print(pop[i], fitness)
    return fitness


# In[330]:


def crossover(a, b):
    child = ''
    midpoint = random.randint(0, len(a))
    #print(midpoint)
    for i in range(len(a)):
        if i > midpoint:
            child = child + a[i]
        else: 
            child = child + b[i]
    return child


# In[331]:


def mutate(mutation_rate):
    triggered = False
    for i in range(len(child)):
        if random.random() < mutation_rate:
            child.replace(child[i], random.choice(string.ascii_lowercase), 1)
            triggered = True
    return child, triggered


# In[333]:


target = args.target
pop = population(900)
mutation_rate = args.mutation
generation = 1
goal = False
while goal == False:
    fit = []
    for i in range(len(pop)):
        fit.append(fitness(target, pop[i]))
        
    mating_pool = []
    for i in range(len(pop)):
        n = int(fit[i] * 100)
        for j in range(n):
            mating_pool.append(pop[i])
            
    for i in range(len(pop)):
        a = random.randint(0, len(mating_pool)-1)
        b = random.randint(0, len(mating_pool)-1)
        
        parent_a = mating_pool[a]
        parent_b = mating_pool[b]
        
        child = crossover(parent_a, parent_b)
        child, triggered = mutate(mutation_rate)
        pop[i] = child
        
    avg_fitness = sum(fit)/len(fit)
    max_fitness_idx = fit.index(max(fit))
    max_fit_word = pop[max_fitness_idx]
    if generation % 10 == 0:
        print('Avg Fitness: {}\t Generation: [{}]\t Word: {}\t Mutation: {}'.format(avg_fitness, generation, max_fit_word, triggered))
    if max_fit_word == target:
        goal = True
        print('Avg Fitness: {}\t Generation: [{}]\t Word: {}\t Mutation: {}'.format(avg_fitness, generation, max_fit_word, triggered))
        
    generation += 1




# In[ ]:




