import unittest
from algorithms.brute_force import fractional_knapsack_brute_force, knapsack_01_brute_force
from algorithms.greedy import fractional_knapsack_greedy
from algorithms.dynamic_programming import knapsack_01_dynamic

class TestKnapsackAlgorithms(unittest.TestCase):

    def test_fractional_knapsack_brute_force(self):
        n = 3
        capacity = 50
        weights = [10, 20, 30]
        profits = [60, 100, 120]
        expected = ([1, 1, 0.6666666666666666], 50, 240.0)
        result = fractional_knapsack_brute_force(n, capacity, weights, profits)
        self.assertEqual(result[0], expected[0])
        self.assertEqual(result[1], expected[1])
        self.assertAlmostEqual(result[2], expected[2], places=6)

    def test_knapsack_01_brute_force(self):
        n = 4
        capacity = 50
        weights = [10, 20, 30, 40]
        profits = [60, 100, 120, 200]
        expected = ([1, 1, 0, 0], 30, 160)
        result = knapsack_01_brute_force(n, capacity, weights, profits)
        self.assertEqual(result, expected)

    def test_fractional_knapsack_greedy(self):
        profits = [60, 100, 120]
        weights = [10, 20, 30]
        capacity = 50
        expected = (240.0, [1.0, 1.0, 0.6666666666666666])
        result = fractional_knapsack_greedy(profits, weights, capacity)
        self.assertAlmostEqual(result[0], expected[0], places=6)
        self.assertEqual(result[1], expected[1])

    def test_knapsack_01_dynamic(self):
        n = 4
        capacity = 50
        profits = [60, 100, 120, 200]
        weights = [10, 20, 30, 40]
        expected = 300
        result = knapsack_01_dynamic(n, capacity, profits, weights)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()