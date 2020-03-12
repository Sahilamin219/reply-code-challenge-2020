import numpy as np


class problem():
    def __init__(self, filename: str):
        with open(filename) as f:
            lines = f.readlines()
            N, M, C, R = lines[0].replace('\n', '').split(sep=' ')
            self.N = int(N)  # width
            self.M = int(M)  # height
            self.C = int(C)
            self.R = int(R)
            self.customers = []  # list of (x, y, reward) customer locations and rewards
            self.set_customers(lines[1:self.C+1])
            self.mappa = self.make_map(lines[self.C+1:])

    def set_customers(self, customer_data: list) -> None:
        for line in customer_data:
            self.customers.append(line.replace('\n', '').split(sep=' '))

    def make_map(self, map_data: list) -> np.array:
        mapp = []
        for line in map_data:
            line.replace('\n', '')
            row = []
            for char in line[:self.N]:
                char = char.replace('#', '1000000000')  # mountain
                char = char.replace('~', '800')  # water
                char = char.replace('*', '200')  # traffic jam
                char = char.replace('+', '150')  # dirt
                char = char.replace('X', '120')  # railway
                char = char.replace('_', '100')  # terrain
                char = char.replace('H', '70')   # highway
                char = char.replace('T', '50')   # railway
                row.append(int(char))
            mapp.append(row)
        return np.asarray(mapp)


if __name__ == '__main__':
    p = problem('/home/pjk/Documents/reply-code-challenge-2020/1_victoria_lake.txt')
    print(p.mappa)
