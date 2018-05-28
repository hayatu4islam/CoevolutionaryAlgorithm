import random
import copy
import sys

# Constants
pic_width  = 5
pic_height = 5

class Creator:
    x = 0
    y = 0
    genes = []
    fitness = 0

    def __init__(self):
        for i in range(pic_width * pic_height):
            self.genes.append(random.randint(0, 1))

    # Fills the scores array based on the input from each of criticsself.
    def critique(self, critics):
        total_score = 0
        for index, critic in enumerate(critics):
            score = 0
            for i in range(pic_width * pic_height):
                if((critic.genes[i]) ^ (self.genes[i])):
                    score += 1
            critic.scores[index] = score
            total_score += score 
        self.fitness = total_score / len(critics)

    def print(self):
        for y in range(pic_height):
            for x in range(pic_width):
                char = '*' if self.genes[(x + y*pic_width)] > 0 else ' '
                print(char, end='')
            print()

class Critic:
    x = 0
    y = 0
    genes = []
    fitness = 0
    scores = []
    inv_vars = []

    def __init__(self):
        for i in range(pic_width * pic_height):
            self.genes.append(random.randint(0, 1))
            self.scores.append(0)
            self.inv_vars.append(0)

    def converge(self, creators):
        for index, creator in enumerate(creators):
            if (self.scores[index] - creator.fitness)**2 < 1:
                self.inv_vars[index] = 1
            else:
                self.inv_vars[index] = 1/(self.scores[index] - creator.fitness)**2
            self.fitness = sum(self.inv_vars)
    
    def print(self):
        for y in range(pic_height):
            for x in range(pic_width):
                char = '*' if self.genes[(x + y*pic_width)] > 0 else ' '
                print(char, end='')
            print()

class Pool:
    #Hyperparameters
    num_critics = 5
    num_creators = 5
    fitness_limit = (num_critics + pic_width * pic_height)*.9

    creators = []
    critics = []
    generation_count = 0
    max_fitness = -1


    # Index values corresponding to the best of the most recent generation
    fittest_creator = Creator()
    second_fittest_creator = Creator()
    fittest_critic = Critic()
    second_fittest_critic = Critic()

    # Constructor - fills creators/critics and gets the initial fitness values
    def __init__(self):

        for i in range(self.num_creators):
            self.creators.append(Creator())
        for i in range(self.num_critics):
            self.critics.append(Critic())

        #Compute fitness
        self.compute_fitness()

    def selection(self):
        # Get fittest creator
        fittest_creator = self.get_fittest_creator()
        # Get second fittest creator
        second_fittest_creator = self.get_second_fittest_creator()
        # Get fittest critic
        fittest_critic = self.get_fittest_critic()
        # Get second fittest critic
        second_fittest_critic = self.get_second_fittest_critic()

    def crossover(self):
        # Select a random crossover point for creators
        crosspoint = random.randint(0, pic_width * pic_height)
        for i in range(crosspoint):
            temp = self.fittest_creator.genes[i]
            self.fittest_creator.genes[i] = self.second_fittest_creator.genes[i]
            self.second_fittest_creator.genes[i] = temp

        # Select a random crossover point for critics
        crosspoint = random.randint(0, pic_width * pic_height)
        for i in range(crosspoint):
            temp = self.fittest_critic.genes[i]
            self.fittest_critic.genes[i] = self.second_fittest_critic.genes[i]
            self.second_fittest_critic.genes[i] = temp

    def mutation(self):
        # Select random mutation points for creators
        mutationpoint = random.randint(0, pic_width * pic_height)

        if self.fittest_creator.genes[mutationpoint] == 1:
            self.fittest_creator.genes[mutationpoint] = 0
        else:
            self.fittest_creator.genes[mutationpoint] = 1

        mutationpoint = random.randint(0, pic_width * pic_height)

        if self.second_fittest_creator.genes[mutationpoint] == 1:
            self.second_fittest_creator.genes[mutationpoint] = 0
        else:
            self.second_fittest_creator.genes[mutationpoint] = 1
        # Select random mutation points for critics
        mutationpoint = random.randint(0, pic_width * pic_height)

        if self.fittest_critic.genes[mutationpoint] == 1:
            self.fittest_critic.genes[mutationpoint] = 0
        else:
            self.fittest_critic.genes[mutationpoint] = 1

        mutationpoint = random.randint(0, pic_width * pic_height)

        if self.second_fittest_critic.genes[mutationpoint] == 1:
            self.second_fittest_critic.genes[mutationpoint] = 0
        else:
            self.second_fittest_critic.genes[mutationpoint] = 1

    def add_fittest_offspring(self):
        self.fittest_creator.critique(self.critics)
        self.second_fittest_creator.critique(self.critics)

        self.fittest_critic.converge(self.creators)
        self.second_fittest_critic.converge(self.creators)

        new_creator = self.fittest_creator
        new_critic = self.fittest_critic

        if self.fittest_creator.fitness < self.second_fittest_creator.fitness:
            new_creator = self.second_fittest_creator

        if self.fittest_critic.fitness < self.second_fittest_critic.fitness:
            new_critic = self.second_fittest_critic

        creator_min_index = self.creators.index(min(self.creators, key=lambda creator: creator.fitness))
        critic_min_index = self.critics.index(min(self.critics, key=lambda critic: critic.fitness))

        pool.creators[creator_min_index] = new_creator
        pool.critics[critic_min_index] = new_critic

    def compute_fitness(self):
        for creator in self.creators:
            creator.critique(self.critics)
        for critic in self.critics:
            critic.converge(self.creators)
        self.max_fitness = max(self.creators, key=lambda creator: creator.fitness).fitness + max(self.critics, key=lambda critic: critic.fitness).fitness

    # Helper functions

    def get_fittest_creator(self):
        temp = sorted(self.creators, key=lambda creator: creator.fitness)[-1]
        return copy.copy(temp)

    def get_second_fittest_creator(self):
        temp = sorted(self.creators, key=lambda creator: creator.fitness)[-2]
        return copy.copy(temp)

    def get_fittest_critic(self):
        temp = sorted(self.critics, key=lambda critic: critic.fitness)[-1]
        return copy.copy(temp)

    def get_second_fittest_critic(self):
        temp = sorted(self.critics, key=lambda critic: critic.fitness)[-1]
        return copy.copy(temp)

if __name__ == "__main__":
    #Generate the initial population
    pool = Pool()

    if len(sys.argv) > 1:
        pool.fitness_limit = float(sys.argv[1])

    #Repeat until the population has converged:
    print(str(pool.max_fitness) + ' ' + str(pool.fitness_limit))
    while(pool.max_fitness < pool.fitness_limit):
        pool.generation_count += 1
        # Selection
        pool.selection()
        # Crossover
        pool.crossover()
        # Mutation
        if random.randint(0, 10) < 8 :
            pool.mutation()

        # Offsprint
        pool.add_fittest_offspring()

        # Compute fitness
        pool.compute_fitness()

        if pool.generation_count % 100 == 1 :

            print("Generation: " + str(pool.generation_count))
            print("Fittest Creator: " + str(pool.max_fitness))
            pool.fittest_creator.print()

            print("Fittest critic: " + str(pool.fittest_critic.fitness))
            pool.fittest_critic.print()
            # print("Critics:")
            # for critic in pool.critics:
            #     critic.print()

    # Print the result
    print("True art: ")
    pool.fittest_creator.print()
    # Stop
