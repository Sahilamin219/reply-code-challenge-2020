'''
    Computes potentials and fitness
'''
from data_models import Resource


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
