'''
    Computes potentials and fitness
'''
from data_models import Resource, ProblemInstance
import numpy as np


def total_potential(r_1: Resource, r_2: Resource):
    '''
        :param r_1: Resource Object
        :param r_2: Resource Object
        :return: Total potential as described in equation 3
    '''
    union_size = len(r_1.skill_set.union(r_2.skill_set))
    inter_size = len(r_1.skill_set.intersection(r_2.skill_set))
    work_pot = inter_size*(union_size - inter_size)
    bonus_pot = (r_1.bonus * r_2.bonus)*(r_1.company == r_2.company)
    return work_pot+bonus_pot


def fitness(prob_inst, dev_loc, man_loc):
    # Change to list of tuple, each tuple is a coordinate in the map
    all = dev_loc + man_loc
    all_loc_dict = {loc: i for i, loc in enumerate(all)}
    all_couple_loc = set()
    for loc in all:
        # Take only not empty tumples
        if loc == ():
            continue
        # nearest positions
        loc_t = (loc[0], loc[1]+1)
        loc_b = (loc[0], loc[1]-1)
        loc_r = (loc[0]+1, loc[1])
        loc_l = (loc[0]-1, loc[1])
        # update only if exist
        if loc_t in all:
            all_couple_loc.update({loc, loc_t})
        if loc_b in all:
            all_couple_loc.update({loc, loc_b})
        if loc_r in all:
            all_couple_loc.update({loc, loc_r})
        if loc_l in all:
            all_couple_loc.update({loc, loc_l})
    # change set of set in list of tuple
    all_couple_list = list(tuple(c) for c in all_couple_loc)
    all_r = prob_inst.developer_list + prob_inst.mangers_list
    all_couple_r = [[all_r[all_loc_dict[x]], all_r[all_loc_dict[y]]] for x, y in all_couple_list]
    return sum(total_potential(couple_r[0], couple_r[1]) for couple_r in all_couple_r)



