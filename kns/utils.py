from copy import deepcopy

def minimize_permutation(in_permutation) -> list:
    in_sorted = sorted(in_permutation)
    return [in_sorted.index(i) for i in in_permutation]


def generate_permutations(l, ones, left, out):
    if ones > left:
        return
    if left == 1:
        if ones:
            out.append(l + [1])
        else:
            out.append(l + [0])
    generate_permutations(l + [0], ones, left-1, out)
    if ones:
        generate_permutations(l + [1], ones-1, left-1, out)


def extract_list(input_list, permutation):
    out1 = []
    out2 = []
    for i, elem in enumerate(input_list):
        if permutation[i]:
            out1.append(elem)
        else:
            out2.append(elem)
    return out1, out2


def has_twins(in_list, min_twins=2, twins=None):
    for length in range(min_twins*2, len(in_list) + 1, 2):
        idx = 0
        permutations = []
        generate_permutations([], length / 2, length, permutations)
        while idx + length <= len(in_list):
            for permutation in permutations:
                perm1, perm2 = extract_list(in_list[idx:idx+length], permutation)
                perm1_ = minimize_permutation(perm1)
                perm2_ = minimize_permutation(perm2)
                if perm1_ == perm2_:
                    if twins:
                        twins.p1 = perm1
                        twins.p2 = perm2
                    return True
            idx += 1
    return False


def add_number_to_permutation(permutation, position, number):
    out = deepcopy(permutation)
    out.insert(position, number)
    return out


def test_candidates_for_position(permutation, min_len, available_numbers, position):
    candidates = []
    for number in available_numbers:
        tmp = add_number_to_permutation(permutation, position, number)
        if not has_twins(tmp, min_len):
            candidates.append(number)
    return candidates

