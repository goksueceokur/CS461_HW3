from math import inf

TREE_DEPTH = 2
BRANCH_FACTOR = 3
ALPHABET = ['A','B','C','D','E','F','G','H','I']

def alpha_beta(input_list, is_minimizing, depth = 0, index = 0, alpha=-inf, beta=inf, trace_mod=False):
    if depth == TREE_DEPTH:
        parent_index = (index - 1) // BRANCH_FACTOR
        child_no = index - parent_index * BRANCH_FACTOR
        child_direction = ""
        if child_no == 1:
            child_direction = "LEFT"
        elif child_no == 2:
            child_direction = "MIDDLE"
        elif child_no == 3:
            child_direction = "RIGHT"

        non_leaf_nodes = sum(BRANCH_FACTOR ** i for i in range(TREE_DEPTH ))
        value = int(input_list[index - non_leaf_nodes])

        if trace_mod:
            print(('\t' * depth), child_direction, "node at depth", depth, "has a value", value)

        return child_direction, value

    if trace_mod:
        turn = "minimizer" if is_minimizing else "maximizer"
        print(('\t' * depth), "Turn of", turn)    
    
    if is_minimizing:
        count = 0 #!
        min_children = inf
        direction = ""
        while count < BRANCH_FACTOR and alpha < beta:
            if trace_mod:
                if count == 0:
                    print(('\t' * depth), "Going LEFT")
                elif count == 1:
                    print(('\t' * depth), "Going MIDDLE")
                elif count == 2:
                    print(('\t' * depth), "Going RIGHT")

            child_direction, temp_value = alpha_beta(input_list, not is_minimizing, depth + 1, index * BRANCH_FACTOR + count + 1, alpha, beta, trace_mod)

            if temp_value < min_children:
                min_children = temp_value
                if count == 0:
                    direction = "LEFT"
                elif count == 1:
                    direction = "MIDDLE"
                elif count == 2:
                    direction = "RIGHT"

            beta = min(beta, temp_value)
            count += 1

        if alpha >= beta:
            while count < BRANCH_FACTOR:
                print_pruned(input_list, depth + 1, index * BRANCH_FACTOR + count + 1)
                count += 1

        if trace_mod:
            print(('\t' * depth), turn, "chose", direction, "node at depth", depth, "and has a value", min_children)

        return direction, min_children

    if not is_minimizing:
        count = 0 #!
        max_children = -inf
        direction = ""
        while count < BRANCH_FACTOR and alpha < beta:
            child_direction, temp_value = alpha_beta(input_list, not is_minimizing, depth + 1, index * BRANCH_FACTOR + count + 1, alpha, beta, trace_mod)
            
            if temp_value > max_children:
                max_children = temp_value
                if count == 0:
                    direction = "LEFT"
                elif count == 1:
                    direction = "MIDDLE"
                elif count == 2:
                    direction = "RIGHT"

            alpha = max(alpha, temp_value)
            count += 1

        if alpha >= beta:
            while count < BRANCH_FACTOR:
                print_pruned(input_list, depth + 1, index * BRANCH_FACTOR + count + 1)
                count += 1
                
        if trace_mod:
            print(('\t' * depth), turn, "chose", direction, "node at depth", depth, "and has a value", max_children)

        return direction, max_children

def print_pruned(input_list, depth, index):
    if depth == TREE_DEPTH:
        non_leaf_nodes = sum(BRANCH_FACTOR ** i for i in range(TREE_DEPTH ))
        print(('\t' * depth), "Node {} with value {} is pruned".format(ALPHABET[index - non_leaf_nodes], input_list[index - non_leaf_nodes]))
        return

    else:
        print("Error")

def main():
    takenInput = input("give input: ")
    userInput = takenInput.split(" ")
    for i in userInput:
        i= int(i)
    starter = "maximizer" # other option is "minimizer"
    choice = input("Do you want to enable single stepping? Y/N \n") in ["Y", "y", "yes", "Yes"]
    
    result = alpha_beta(userInput, False, trace_mod = choice)
    if choice:  
        print("--------------")

    print("Selected move for", starter, "is", result[0], "and has a value", result[1])

if __name__ == '__main__':
    main()
    