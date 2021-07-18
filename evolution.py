from player import Player
import numpy as np
from config import CONFIG
from copy import copy


class Evolution():

    def __init__(self, mode):
        self.mode = mode

    # calculate fitness of players
    def calculate_fitness(self, players, delta_xs):
        for i, p in enumerate(players):
            p.fitness = delta_xs[i]

    def mutate(self, child):

        # TODO
        # child: an object of class `Player`
        pm = 0.05
        mean = 0
        variance = 0.01
        for w in child.nn.w:
            num_rows, num_cols = w.shape
            for x in range(num_rows):
                for y in range(num_cols):
                    if np.random.uniform(0, 1, 1) < pm:
                        w[x, y] += np.random.normal(mean, variance, 1)
                        if w[x, y] > 1:
                            w[x, y] = 1
                        elif w[x, y] < -1:
                            w[x, y] = -1

        for b in child.nn.b:
            num_rows, num_cols = b.shape
            for x in range(num_rows):
                for y in range(num_cols):
                    if np.random.uniform(0, 1, 1) < pm:
                        b[x, y] += np.random.normal(mean, variance, 1)
                        if b[x, y] > 1:
                            b[x, y] = 1
                        elif b[x, y] < -1:
                            b[x, y] = -1

        pass


    def generate_new_population(self, num_players, prev_players=None):

        # in first generation, we create random players
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]

        else:

            # TODO
            # num_players example: 150
            # prev_players: an array of `Player` objects

            # parent selection with roulette wheel approach
            # total_fitness = sum(p.fitness for p in prev_players)
            # uniform_rnd_numb = sorted(np.random.uniform(0, 1, num_players))
            # index = 0
            # current = 0
            # new_players = []
            # for p in prev_players:
            #     current += p.fitness / total_fitness
            #     while index < num_players and current > uniform_rnd_numb[index]:
            #         # create new child from selected parent
            #         new_players.append(copy(p))
            #         index += 1

            # parent selection with SUS approach
            total_fitness = sum(p.fitness for p in prev_players)
            rnd_num = np.random.rand() / num_players
            step = 0
            current = 0
            new_players = []
            for p in prev_players:
                current += p.fitness / total_fitness
                while current > rnd_num and step < num_players:
                    new_players.append(copy(p))
                    step += 1
                    rnd_num += 1 / num_players

            for child in new_players:
                self.mutate(child)

            # TODO (additional): a selection method other than `fitness proportionate`
            # TODO (additional): implementing crossover

            # new_players = prev_players
            return new_players

    def next_population_selection(self, players, num_players):

        # TODO
        # num_players example: 100
        # players: an array of `Player` objects
        players.sort(key=lambda x: x.fitness, reverse=True)

        # TODO (additional): a selection method other than `top-k`
        # TODO (additional): plotting

        return players[: num_players]
