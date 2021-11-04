class InvalidStatesException(Exception):
    pass


def make_markov_chain_generator(state_table):
    if (not isinstance(state_table, list)) or (not len(state_table) > 0):
        raise InvalidStatesException

    def gen():
        while True:
            yield 0

    return gen()