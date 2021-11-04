class InvalidStatesException(Exception):
    pass


def make_markov_chain_generator(state_table):
    if (not isinstance(state_table, list)) or (not len(state_table) > 0) or any(
            sum(state_table[i]) != 1 for i in range(len(state_table))):
        raise InvalidStatesException

    def gen():
        state = 0
        while True:
            yield state
            state = state_table[state].index(1)

    return gen()
