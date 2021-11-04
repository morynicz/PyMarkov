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

    def test_given_chain_with_two_alternating_states_when_generates_repeatedly_then_returns_0_1_0_1(self):
        sut = make_markov_chain_generator([[0, 1], [1, 0]])
        self.assertEqual([0, 1, 0, 1], [next(sut) for i in range(4)])

    def test_given_chain_with_two_states_with_second_looping_when_generates_repeatedly_then_returns_0_1_1_1(self):
        sut = make_markov_chain_generator([[0, 1], [0, 1]])
        self.assertEqual([0, 1, 1, 1], [next(sut) for i in range(4)])

    def test_given_chain_with_three_circling_states_when_generates_repeatedly_then_returns_0_2_1_0_2(self):
        sut = make_markov_chain_generator([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
        self.assertEqual([0, 2, 1, 0], [next(sut) for i in range(4)])

    def test_given_state_transitions_not_summing_to_1_in_row_when_then_throws_invalid_states_exception(
            self):
        with self.assertRaises(InvalidStatesException):
            make_markov_chain_generator([[0.1]])

    def test_given_state_transitions_not_summing_to_1_in_different_row_then_throws_invalid_states_exception(
            self):
        with self.assertRaises(InvalidStatesException):
            make_markov_chain_generator([[0, 1], [0.9, 0]])

