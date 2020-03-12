import argparse
import io_parsing
import initial_population as ip


if __name__ == '__main__':
    prob = ip.io_parsing.read_problem('a_.txt')
    dev_seats = ip.gimme_dev_seats(prob.board)
    man_seats = ip.gimme_man_seats(prob.board)
    dev = ip.make_population(1, dev_seats, man_seats)[0][0]
    man = ip.make_population(1, dev_seats, man_seats)[0][1]
    io_parsing.write_solution(dev, man)
