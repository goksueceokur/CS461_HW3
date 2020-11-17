from math import inf

TRACE_MOD = True

TREE_DEPTH = 2
BRANCH_FACTOR = 3
EVAL_LIST = [5, 3, 1, 2, 5, 4, 1, 3, 3]
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

def alpha_beta(is_minimizing, depth = 0, index = 0, alpha=-inf, beta=inf):
    if depth == TREE_DEPTH:
        return EVAL_LIST[index - 4]
        
    if is_minimizing:
        count = 0 #!
        min_children = inf
        while count < BRANCH_FACTOR and alpha < beta:
            temp_value = alpha_beta(not is_minimizing, depth + 1, index * BRANCH_FACTOR + count + 1, alpha, beta)
            min_children = min(min_children, temp_value)
            beta = min(beta, temp_value)
            count += 1

        if alpha >= beta:
            while count < BRANCH_FACTOR:
                print_pruned(depth + 1, index * BRANCH_FACTOR + count + 1)
                count += 1

        return min_children

    if not is_minimizing:
        count = 0 #!
        max_children = -inf
        while count < BRANCH_FACTOR and alpha < beta:
            temp_value = alpha_beta(not is_minimizing, depth + 1, index * BRANCH_FACTOR + count + 1, alpha, beta)
            max_children = max(max_children, temp_value)
            alpha = max(alpha, temp_value)
            count += 1

        if alpha >= beta:
            while count < BRANCH_FACTOR:
                print_pruned(depth + 1, index * BRANCH_FACTOR + count + 1)
                count += 1

        return max_children

def print_pruned(depth, index):
    if depth == TREE_DEPTH:
        print("Node {} with value {} is pruned".format(ALPHABET[index - 4], EVAL_LIST[index - 4]))
        return

    else:
        print("Sıçtık")


def main():
    print(alpha_beta(False))
    pass

if __name__ == '__main__':
    main()
    