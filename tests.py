import unittest

from MarkovChainGenerator import InvalidStatesException, make_markov_chain_generator


class MarkovChainGeneratorTestSuite(unittest.TestCase):
    def test_when_chain_without_state_traversal_matrix_creation_attempted_then_throw_invalid_states_exception(self):
        with self.assertRaises(InvalidStatesException):
            make_markov_chain_generator(None)

    def test_when_chain_with_empty_state_traversal_matrix_creation_attempted_then_throw_invalid_states_exception(self):
        with self.assertRaises(InvalidStatesException):
            make_markov_chain_generator([])

    def test_given_chain_with_one_state_when_generates_then_returns_0(self):
        sut = make_markov_chain_generator([[1]])
        self.assertEqual(0, next(sut))

    def test_given_chain_with_one_state_when_generates_multiple_times_then_always_returns_0(self):
        sut = make_markov_chain_generator([[1]])
        self.assertEqual([0, 0, 0, 0, 0], [next(sut) for i in range(5)])



if __name__ == '__main__':
    unittest.main()
