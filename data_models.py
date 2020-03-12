from typing import List, Set


class ProblemInstance():
    board = None
    developer_list: List = list()
    manager_list: List = list()

    def __init__(self, board, developer_list=None, manager_list=None):
        self.board = board

        if developer_list is not None:
            self.developer_list = developer_list

        if manager_list is not None:
            self.manager_list = manager_list


class Resource():
    company = None
    bonus = None
    skill_set: Set[str] = set()

    def __init__(self, company, bonus, skill_set=None):
        self.company = company
        self.bonus = bonus

        if skill_set is not None:
            self.skill_set = skill_set

    def add_skill(self, skill):
        self.skill_set.add(skill)


if __name__ == "__main__":
    d_list = [1, 2, 3]
    m_list = [1, 2, 3]
    a = ProblemInstance(1, d_list, m_list)
    print(a)
