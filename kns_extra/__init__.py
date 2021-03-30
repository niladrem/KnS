from kns.twins import Twins
from kns.utils import has_twins
import itertools


def main():
    input_list = [1, 2, 3, 4, 5, 6]
    permutation_list = itertools.permutations(input_list)

    for permutation in permutation_list:
        print("\nCurrent permutation: %s" % str(permutation))
        twins = Twins()
        has_twins(permutation, twins)
        twins.print_twins()


if __name__ == "__main__":
    main()
