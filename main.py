import argparse
import io_parsing
import initial_population as ip


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'input_file',
        type=str)

    arguments_list = parser.parse_args()

    prob = io_parsing.read_problem(arguments_list.input_file)
    dev_seats = ip.gimme_dev_seats(prob.board)
    man_seats = ip.gimme_man_seats(prob.board)
    dev = ip.make_population(prob, 1, dev_seats, man_seats)[0][0]
    man = ip.make_population(prob, 1, dev_seats, man_seats)[0][1]
    io_parsing.write_solution(dev, man)
