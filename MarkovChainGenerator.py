from itertools import accumulate


class InvalidStatesException(Exception):
    pass


def make_markov_chain_generator(state_table, rng):
    if (not isinstance(state_table, list)) or (not len(state_table) > 0) or any(
            sum(state_table[i]) != 1 for i in range(len(state_table))):
        raise InvalidStatesException

    distributions = [[y for y in accumulate(x)] for x in state_table]

    def gen():
        state = 0
        while True:
            yield state
            roll = next(rng)
            state = next(st for st, weight in enumerate(distributions[state]) if weight > roll)
    return gen()
