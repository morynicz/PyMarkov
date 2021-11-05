import argparse
import json

import MarkovChainGenerator as mg


def generate_sequence(states_table, length):
    markov = mg.make_markov_chain_generator(states_table)
    return [next(markov) for x in range(length)]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("state_transitions_table", action='store',
                        help="Json file with 2d table of transition probabilities. Example: [[0, 1],[1, 0]] will certainly go from state 0 to 1 and back. [[0.9, 0.1], [0,1]] will start in 0, has small probability to go to 1 and will stay in 1 forever.")
    parser.add_argument("length", action='store', type=int, help="Length of sequence to generate")
    args = parser.parse_args()
    with open(args.state_transitions_table) as t:
        states = json.load(t)
        print(generate_sequence(states, args.length))
