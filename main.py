from kns.twins import Twins
from kns.utils import has_twins, test_candidates_for_position, add_number_to_permutation
import random


def main():
    n = input("Podaj dlugosc permutacji: ")
    n = int(n)
    k = input("Podaj minimalną długość ciasnego bliźniaka (domyślnie 2): ")
    try:
        k = int(k)
        if k < 1:
            k = 2
    except:
        k = 2

    out = loop(n, k)
    if out:
        print("Wygrał gracz")
    else:
        print("Wygrał człowiek")


def loop(n, k):
    current_permutation = []
    available_numbers = [i for i in range(1, n+1)]
    while len(available_numbers):
        print_current_permutation(current_permutation)
        idx = get_position(len(current_permutation) + 1)
        candidates = test_candidates_for_position(current_permutation, k, available_numbers, idx)
        if len(candidates):
            tmp = random.choice(candidates)
            current_permutation = add_number_to_permutation(current_permutation, idx, tmp)
            available_numbers.remove(tmp)
        else:
            current_permutation = add_number_to_permutation(current_permutation, idx, available_numbers[0])
            available_numbers.remove(available_numbers[0])
            print("Permutacja: %s" % str(current_permutation))
            twins = Twins()
            has_twins(current_permutation, k, twins)
            print("Ciasne bliźniaki: %s, %s" % (str(twins.p1), str(twins.p2)))
            return True

    print("Permutacja: %s" % str(current_permutation))
    return False


def get_position(max_pos):
    while True:
        k = input("Podaj pozycję: ")
        k = int(k)
        if k < 0 or k > max_pos:
            print("Niepoprawna pozycja")
        else:
            return k


def print_current_permutation(permutation):
    out = ""
    for i, elem in enumerate(permutation):
        out += " [" + str(i) + "] " + str(elem)
    out += " [" + str(len(permutation)) + "]"
    print(out)


if __name__ == '__main__':
    main()
