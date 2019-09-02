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


#Generates a random word between the ascii numbers 32 and 127
#These numbers correspond to characters 'a-z', 'A-Z', '0-9' and special characters like '$', '!', '%' etc
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

#This function takes in an integer, which decides the size of our population
#and appends it to the list 'pop'
def population(size):
    pop = []
    for i in range(size):
        pop.append(random_word_generator(len(target)))
    return pop


# In[329]:

#This is where the fitness of each word is calculated
#It first checks if the word in the population has characters that are also present in the target word
#Then it checks if theses characters are in the same location as in the target word
#If yes, then it increments the score variable
#Finally it calculates the fitness by dividing the score with the length of the word.
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

#This is the crossover function which takes the traits of either parent(word from population) and then 
#copies it to the child(new word)
#Midpoint is a random index, which serves as the condition for whether the child gets traits from parent a or parent b. 
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

#The mutate function simply changes one character in the word, with some % chance. 
#The mutation rate decides this % chance. 
#We generate a random value between 0 and 1, and if this value is less thant our mutation rate, 
#then the character is changed randomly to one of the characters withing the ascii range of 32 and 127
def mutate(mutation_rate):
    triggered = False
    char_list = []
    for j in range(32, 127):
        char_list.append(chr(j))
    for i in range(len(child)):
        if random.random() < mutation_rate:
            child.replace(child[i], random.choice(char_list), 1)
            triggered = True
    return child, triggered


# In[333]:

#Decide the target
target = args.target

#Set population size
pop = population(900)

#Set mutation rate
mutation_rate = args.mutation

#Initialize generation
generation = 1

#Set goal variable to false. This is set to True only when the generated word is the same as the target word,
goal = False

#Loop over the generations
while goal == False:
    #Calcualte fitness
    fit = []
    for i in range(len(pop)):
        fit.append(fitness(target, pop[i]))
        
    #Create the mating pool 
    mating_pool = []
    for i in range(len(pop)):
        n = int(fit[i] * 100)
        for j in range(n):
            mating_pool.append(pop[i])
        
    #Make the child word and mutate
    for i in range(len(pop)):
        a = random.randint(0, len(mating_pool)-1)
        b = random.randint(0, len(mating_pool)-1)
        
        parent_a = mating_pool[a]
        parent_b = mating_pool[b]
        
        child = crossover(parent_a, parent_b)
        child, triggered = mutate(mutation_rate)
        pop[i] = child
       
    #Calculate average fitness
    avg_fitness = sum(fit)/len(fit)
    
    #Get word with max fitness
    max_fitness_idx = fit.index(max(fit))
    max_fit_word = pop[max_fitness_idx]
    
    #Print results
    if generation % 10 == 0:
        print('Avg Fitness: {}\t Generation: [{}]\t Word: {}\t Mutation: {}'.format(avg_fitness, generation, max_fit_word, triggered))
    
    #Check if the max fitness word is the same as the target
    if max_fit_word == target:
        goal = True
        print('Avg Fitness: {}\t Generation: [{}]\t Word: {}\t Mutation: {}'.format(avg_fitness, generation, max_fit_word, triggered))
    
    #Increment the generation
    generation += 1




# In[ ]:




