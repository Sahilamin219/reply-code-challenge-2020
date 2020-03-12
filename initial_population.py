# input: ProblemInstance
# ProblemInstance -> feasible_developer_seats(list) [D], feasible_manager_seats(list) [M]
# seat: tuple (x, y)
# initial_population(d, m) -> d \in feasible_developer_seats, m \in feasible_manager_seats
import random
import numpy as np
import io_parsing


def gimme_dev_seats(board: np.array) -> list:
    board = np.array(board)
    return np.argwhere(board == 1)


def gimme_man_seats(board: np.array) -> list:
    board = np.array(board)
    return np.argwhere(board == -1)


def populate_res(res_list: list,
                 res_seats: list) -> list:
    chromosome_len = min(len(res_list), len(res_seats))
    chromosome_lists = random.sample(list(res_seats), chromosome_len)
    chromosome = []
    for item in chromosome_lists:
        chromosome.append((item[0], item[1]))
    if len(res_list) > len(res_seats):
        for item in range(len(res_list) - len(res_seats)):
            chromosome.append(tuple())
    return chromosome


def make_population(prob,
                    size: int,
                    dev_seats: list,
                    man_seats: list) -> list:
    population = []
    for i in range(size):
        # genera un cromosoma dei dev
        dev = populate_res(prob.developer_list, dev_seats)
        random.shuffle(dev)
        # genera un cromosoma dei man
        man = populate_res(prob.manager_list, man_seats)
        random.shuffle(man)
        population.append((dev, man))
    return population

# D = [(1,2), (,), (3,4)], |D|= tot developer
# M = [(5,5), (,)], |M|= tot manager
