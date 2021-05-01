from kns.twins import Twins
from kns.utils import has_twins, test_candidates_for_position, add_number_to_permutation, victory, defeat, baner
import random


def main():
    print(baner)
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
        print(defeat)
    else:
        print("Wygrał człowiek")
        print(victory)


def loop(n, k):

    CP1 = '\033[36m'
    CP2 = '\033[35m'
    CEND = '\33[0m'

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

            twins = Twins()
            has_twins(current_permutation, k, twins)

            str_perm = []
            for x in current_permutation:
                if x in twins.p1:
                    str_perm.append(CP1 + str(x) + CEND)
                elif x in twins.p2:
                    str_perm.append(CP2 + str(x) + CEND)
                else:
                    str_perm.append(str(x))

            str_perm = ', '.join(str_perm)
                
            print("Permutacja: [%s]" % str_perm)#str(current_permutation))
            print("Ciasne bliźniaki: %s, %s" % (CP1 + str(twins.p1) + CEND, CP2 + str(twins.p2) + CEND))
            return True

    print("Permutacja: %s" % str(current_permutation))
    return False


def get_position(max_pos):
    while True:
        k = input("Podaj pozycję: ")
        if k == "" or int(k) < 0 or int(k) > max_pos:
            print("Niepoprawna pozycja")
        else:
            return int(k)


def print_current_permutation(permutation):

    CPOZ = '\033[128m'
    CEND = '\033[0m'
    CVAL = '\33[93m'

    out = ""
    for i, elem in enumerate(permutation):
        out += CPOZ + " [" + str(i) + "] " + CEND + CVAL + str(elem) + CEND
    out += CPOZ + " [" + str(len(permutation)) + "]" + CEND
    permutation_str = ', '.join(CVAL + str(x) + CEND for x in permutation)
    out += '\nObecna permutacja: ' + permutation_str
    print(out)


if __name__ == '__main__':
    main()
