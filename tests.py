import unittest
from itertools import repeat

from MarkovChainGenerator import InvalidStatesException, make_markov_chain_generator


class MarkovChainGeneratorTestSuite(unittest.TestCase):
    @staticmethod
    def make_sut(state_table, rng=repeat(0.99)):
        return make_markov_chain_generator(state_table, rng)

    def test_when_chain_without_state_traversal_matrix_creation_attempted_then_throw_invalid_states_exception(self):
        with self.assertRaises(InvalidStatesException):
            self.make_sut(None)

    def test_when_chain_with_empty_state_traversal_matrix_creation_attempted_then_throw_invalid_states_exception(self):
        with self.assertRaises(InvalidStatesException):
            self.make_sut([])

    def test_given_chain_with_one_state_when_generates_then_returns_0(self):
        sut = self.make_sut([[1]])
        self.assertEqual(0, next(sut))

    def test_given_chain_with_one_state_when_generates_multiple_times_then_always_returns_0(self):
        sut = self.make_sut([[1]])
        self.assertEqual([0, 0, 0, 0, 0], [next(sut) for i in range(5)])

    def test_given_chain_with_two_alternating_states_when_generates_repeatedly_then_returns_0_1_0_1(self):
        sut = self.make_sut([[0, 1], [1, 0]])
        self.assertEqual([0, 1, 0, 1], [next(sut) for i in range(4)])

    def test_given_chain_with_two_states_with_second_looping_when_generates_repeatedly_then_returns_0_1_1_1(self):
        sut = self.make_sut([[0, 1], [0, 1]])
        self.assertEqual([0, 1, 1, 1], [next(sut) for i in range(4)])

    def test_given_chain_with_three_circling_states_when_generates_repeatedly_then_returns_0_2_1_0_2(self):
        sut = self.make_sut([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
        self.assertEqual([0, 2, 1, 0], [next(sut) for i in range(4)])

    def test_given_state_transitions_not_summing_to_1_in_row_when_then_throws_invalid_states_exception(
            self):
        with self.assertRaises(InvalidStatesException):
            self.make_sut([[0.1]])

    def test_given_state_transitions_not_summing_to_1_in_different_row_then_throws_invalid_states_exception(
            self):
        with self.assertRaises(InvalidStatesException):
            self.make_sut([[0, 1], [0.9, 0]])

    def test_given_probabilistic_state_transitions_and_rnd_generator_when_generates_then_returns_0_0_1_1(self):
        sut = self.make_sut([[0.5, 0.5], [0, 1]], (x for x in [0.3, 0.6, 0, 0]))
        self.assertEqual([0, 0, 1, 1], [next(sut) for i in range(4)])