import unittest
from kns import twins


class TestUtils(unittest.TestCase):

    def test_is_valid(self):
        t1 = twins.Twins()
        self.assertFalse(t1.is_valid())
        t2 = twins.Twins([1, 2], [3,4])
        self.assertTrue(t2.is_valid())
        t3 = twins.Twins([1, 2])
        self.assertFalse(t3.is_valid())


if __name__ == '__main__':
    unittest.main()
