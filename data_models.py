class ProblemInstance():
    board = None
    developer_list = list()
    manager_list = list()


class Resource():
    company = None
    bonus = None
    skill_set = set()


if __name__ == "__main__":
    a = ProblemInstance()
    a.developer_list = [1, 2, 3]
    print(a)
