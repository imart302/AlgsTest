def backtracking_permutations(arr):
    def backtracking_array(fixed=[], rem=[], ac=[]):
        if len(rem) == 0:
            ac.append(fixed)
            return ac
        else:
            for i in range(0, len(rem)):
                n = rem.pop(i)
                backtracking_array(fixed + [n], rem, ac)
                rem.insert(i, n)

            return ac

    return backtracking_array([], arr, [])


def backtracking_combinations(arr):
    def backtracking_array(fixed=[], rem=[], ac=[]):
        if len(rem) == 0:
            return []
        else:
            for i in range(0, len(rem)):
                n = rem.pop(i)
                ac.append(fixed + [n])
                backtracking_array(fixed + [n], rem, ac)
                rem.insert(i, n)

            return ac

    return backtracking_array([], arr, [])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    combs = backtracking_combinations([1, 2, 3])
    perms = backtracking_permutations([1, 2, 3])
    print("Combinations")
    print(combs)
    print("Permutations")
    print(perms)
