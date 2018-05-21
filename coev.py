import random

# Constants
pic_width = 5
pic_height = 5

#Hyperparameters
fitness limit = 20

class Creator:
    x = 0
    y = 0
    seed = 0

    def __init__(self):
        self.seed = random.randint(0, pic_width * pic_height)

    def compute_fitness(self, critics):
        for critic in critics:
            for i in range

class Critic:
    x = 0
    y = 0
    seed = 0

    def __init__(self):
        self.seed = random.randint(0, pic_width * pic_height)

    def compute_fitness(self, critics):
        for critic in critics:
            for i in range

#Start
if __name__ == "__main__":
    generation = 0
    #Generate the initial population
    creators = []
    critics = []
    for i in range(10):
        creators[i] = Creator()
        critics[i] = Critic()

    #Compute fitness
    max_fitness = compute_fitness()
    #Repeat until the population has converged:
    while(max_fitness < fitness_limit):
        # Selection
        # Crossover
        if(random.randint(0, 10) < 8) {
            Crossover();
        }
        # Mutation
        # Compute fitness
        fitness = compute_fitness()
# Stop
