import random

# Constants
pic_width = 5
pic_height = 5

#Hyperparameters
fitness limit = 20
num_critics = 10
num_creators = 10

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
#Start
if __name__ == "__main__":
    generation = 0
    #Generate the initial population
    creators = []
    critics = []
    for i in range(num_creators):
        creators[i] = Creator()
    for i in range(num_critics):
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
