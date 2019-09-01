# Genetic-Algorithms

[The Nature of Code by Daniel Shiffman](https://natureofcode.com/book/chapter-9-the-evolution-of-code/) gives a very nice background of how genetic algorithms work, along with code in Java. I translated the first program into Python, and made a few changes. 

## Three main properties
Computer Science has been trying to replicate biological phenomenon, in order to achieve different means of arriving at a solution. Neural Networks is a prime example, where the very concept of the network is to replicate how the brain processes information, and now, Neural Networks are termed as "universal approximators". In the same way, **Genetic Algorithms** try to mimic the process of evolution through natural selection. For this, three main properties are considered:
1. Variation
2. Selection
3. Heredity

### Variation
Variation refers to a variation in the DNA of the starting population. In my case, since I am trying to generate target words or sentences, my DNA is the different kinds of characters that I use in my starting population of words. If I am trying to generate a word like 'problem', then I would generate a population of random seven letter words. Size of the population becomes the parameter here. Longer sentences generally require more population, in order to improve. 

### Selection
Once we have a population, we define something called **Fitness**. Fitness is the measure of how good our population is. In my case, since I am trying to generate a word based on a target word, I calculate fitness by counting how many characters for the current word in my population are present in the same location as in the target word, and then divide it by the total number of characters. This gives me a number between 0 and 1, so it can be used as a probability. Once fitness has been calculated for all the words, I need to define something called the **Mating Pool**. The mating pool will contain all the words whose fitness is the highest. I multiply all the fitness values by 100 - let's call that number ***n***. If our target word is **problem**, the word in my population is **g!53lem**, which means 3/7 words are in the correct place. Therefore this word in the population will have a fitness of 0.42. This word has a 42% chance of getting selected in the mating pool. I do this for all the words in the population and fill up the mating pool. This process is referred to as **"Survival of the fittest"**, as only the high fitness words are selected to mate and give offsprings. 

### Heredity
After filling up the mating pool with all the high fitness candidates, a random index from the mating pool is selected for two parents. Then a corresponding parent word is selected from the mating pool. The way that heredity works here is that, I select a midpoint index based on the length of my word, and iterate through the word. If the current index is less than midpoint, then the new child word will get the traits of second parent (by second parent, I mean the second word we got from the mating pool by random selection), and if the current index is greater than the midpoint, then traits of the first parent are inherited. I have also added a term called **Mutation Rate**, which I have set to 1%. This means that there is a 1% chance of any one character of the child getting mutated to a random character. Mutation helps with longer sentences, and differing the value of mutation rate may generate the target word in a lesser number of iterations, or may keep generating random words and never get to the target word at all. 


**Selection** and **Mutation** are repeated in a loop, till the target word is achieved, and each time a new child is created, it replaces a word in the population, signifying the **New Generation**. 
