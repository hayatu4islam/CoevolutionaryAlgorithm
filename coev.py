import random

# Constants
pic_width = 5
pic_height = 5

class Pool:
    #Hyperparameters
    fitness limit = 20
    num_critics = 10
    num_creators = 10

    creators = []
    critics = []
    generation_count = 0
    max_fitness = 0


    # Index values corresponding to the best of the most recent generation
    fittest_creator = -1
    second_fittest_creator = -1
    fittest_critic = -1
    second_fittest_critic = -1

    # Constructor - fills creators/critics and gets the initial fitness values
    def __init__(self):
        for i in range(num_creators):
            self.creators[i] = Creator()
        for i in range(num_critics):
            self.critics[i] = Critic()

        #Compute fitness
        self.compute_fitness()

    def selection():
        # Get fittest creator
        # Get second fittest creator
        # Get fittest critic
        # Get second fittest critic

    def crossover():
        # Select a random crossover point for creators
        # Select a random crossover point for critics
        8
    def mutation():
        # Select random mutation points for creators
        # Select random mutation points for critics

    def compute_fitness():

class Creator:
    x = 0
    y = 0
    seed = 0
    fitness = 0

    def __init__(self):
        self.seed = random.randint(0, pic_width * pic_height)

    # Fills the scores array based on the input from each of criticsself.
    def critique(self, critics):
        for index, critic in enumerate(critics):
            score = 0
            for i in range(pic_width * pic_height):
                if((critic.seed & (1<<i)) ^ (self.seed & (1<<i))):
                    score += 1
            critic.scores[index] = score
        self.fitness = sum(critic.scores)/len(critic.scores)

class Critic:
    x = 0
    y = 0
    seed = 0
    fitness = 0
    scores = []
    inv_vars = []

    def __init__(self):
        self.seed = random.randint(0, pic_width * pic_height)

    def converge(self, creators):
        for index, creator in enumerate(creators):
            if(self.scores[index] == creator.fitness):
                self.inv_vars[index] = 25
            else:
                self.inv_vars[index] = 1/(self.scores[index] - creator.fitness)**2
            self.fitness = sum(self.inv_vars)/len()

if __name__ == "__main__":
    #Generate the initial population
    pool = Pool()

    #Repeat until the population has converged:
    while(pool.max_fitness < fitness_limit):
        # Selection
        pool.selection()
        # Crossover
        pool.crossover()
        # Mutation
        if(random.randint(0, 10) < 8) {
            pool.mutation()
        }
        # Compute fitness
        pool.compute_fitness()

        print("Generation: " + pool.generation_count + " Fittest: " + pool.max_fitness)

    # Print the result
    print("True art: ", end='')
    for y in range(pic_height):
        for x in range(pic_width):
            print(('*' if pool.creators[pool.fittest_creator] & (1 << (x + y*pic_width))) > 0 else ' ')
        print()
    # Stop
