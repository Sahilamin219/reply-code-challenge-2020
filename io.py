import numpy as np
import scipy as sp

import data_models


def read_problem(input_file_name):
    with open(input_file_name, 'r') as input_file:
        # read board shape (X, Y)
        board_shape = tuple(map(int, input_file.readline().split()))
        rows = board_shape[1]
        cols = board_shape[0]

        # read board by lines
        board = np.empty((rows, cols), dtype=int)
        for row_idx in range(rows):
            board_row = list(input_file.readline().strip())
            print(board_row)
            board[row_idx, :] = list(map(convert_board_tile, board_row))
        print(board)

        # read developers list
        developer_num = int(input_file.readline())
        print(developer_num)

        developer_list = list()
        for _ in range(developer_num):
            developer_attrs = input_file.readline().split()
            developer_list.append(
                data_models.Resource(developer_attrs[0],
                                     int(developer_attrs[1]),
                                     developer_attrs[3:]))
        print(developer_list)

        # read managers list
        manager_num = int(input_file.readline())
        print(manager_num)

        manager_list = list()
        for _ in range(manager_num):
            manager_attrs = input_file.readline().split()
            manager_list.append(
                data_models.Resource(manager_attrs[0],
                                     int(manager_attrs[1])))
        print(developer_list)

    return data_models.ProblemInstance(board, developer_list, manager_list)


def convert_board_tile(board_tile):
    if board_tile == '_':
        return 1
    elif board_tile == 'M':
        return -1
    return 0


if __name__ == '__main__':
    p = read_problem('a_solar.txt')
    print(p)
