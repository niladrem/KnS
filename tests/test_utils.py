import unittest
from kns import utils


class TestUtils(unittest.TestCase):

    def test_minimize_permutation(self):
        self.assertEqual(utils.minimize_permutation([1, 2, 3]), [0, 1, 2])
        self.assertEqual(utils.minimize_permutation([3, 5, 1, 2]), [2, 3, 0, 1])
        self.assertEqual(utils.minimize_permutation([3, 1, 6, 2]), [2, 0, 3, 1])
        self.assertEqual(utils.minimize_permutation([2, 1, 0]), [2, 1, 0])

    def test_generate_permutations(self):
        permutations = []
        utils.generate_permutations([], 2, 4, permutations)
        self.assertEqual(sorted(permutations), sorted([[1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1],
                                                       [0, 1, 1, 0], [0, 1, 0, 1], [0, 0, 1, 1]]))

    def test_extract_list(self):
        self.assertEqual(utils.extract_list([1, 2, 3, 4], [0, 1, 1, 0]), ([2, 3], [1, 4]))
        self.assertEqual(utils.extract_list([1, 5, 3, 4], [0, 1, 0, 0]), ([5], [1, 3, 4]))

    def test_has_not_twins(self):
        self.assertFalse(utils.has_twins([0, 1, 2]))
        self.assertFalse(utils.has_twins([0, 3, 2, 1]))

    def test_has_twins(self):
        self.assertTrue(utils.has_twins([2, 5, 8, 4, 1]))
        self.assertTrue(utils.has_twins([0, 1, 4, 3]))
        self.assertTrue(utils.has_twins([1, 2, 3, 4]))
        self.assertTrue(utils.has_twins([1, 5, 4, 2, 6, 5]))


if __name__ == '__main__':
    unittest.main()
