from math import inf

TREE_DEPTH = 2
BRANCH_FACTOR = 3

def minimax(input_list, starter, depth = 0, index = 0, trace_mod=False):
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
        print(('\t' * depth), "Turn of", starter)

    if starter == "minimizer":
        opponent = "maximizer"
        mini = float(inf)
        direction = ""
        for i in range(BRANCH_FACTOR):
            if trace_mod:
                if i == 0:
                    print(('\t' * depth), "Going LEFT")
                elif i == 1:
                    print(('\t' * depth), "Going MIDDLE")
                elif i == 2:
                    print(('\t' * depth), "Going RIGHT")

            child_direction, child_value = minimax(input_list, opponent, depth + 1, index * BRANCH_FACTOR + i + 1, trace_mod)

            if child_value < mini:
                mini = child_value
                if i == 0:
                    direction = "LEFT"
                elif i == 1:
                    direction = "MIDDLE"
                elif i == 2:
                    direction = "RIGHT"

        if trace_mod:
            print(('\t' * depth), starter, "chose", direction, "node at depth", depth, "and has a value", mini)

        return direction, mini
    
    elif starter == "maximizer":
        opponent = "minimizer"
        maxi = float(-inf)
        direction = ""
        for i in range(BRANCH_FACTOR):
            if trace_mod:
                if i == 0:
                    print(('\t' * depth), "Going LEFT")
                elif i == 1:
                    print(('\t' * depth), "Going MIDDLE")
                elif i == 2:
                    print(('\t' * depth), "Going RIGHT")

            child_direction, child_value = minimax(input_list, opponent, depth + 1, index * BRANCH_FACTOR + i + 1, trace_mod)

            if child_value > maxi:
                maxi = child_value
                if i == 0:
                    direction = "LEFT"
                elif i == 1:
                    direction = "MIDDLE"
                elif i == 2:
                    direction = "RIGHT"

        if trace_mod:
             print(('\t' * depth), starter, "chose", direction, "node at depth", depth, "and has a value", maxi)

        return direction, maxi

    else:
        print("An error occured")
        return None, None


def main():
    takenInput = input("give input: ")
    userInput = takenInput.split(" ")
    for i in userInput:
        i= int(i)
    starter = "maximizer" # other option is "minimizer"
    choice = input("Do you want to enable single stepping? Y/N \n") in ["Y", "y", "yes", "Yes"]
    result = minimax(userInput, starter, trace_mod=choice)
    if choice:  
        print("--------------")

    print("Selected move for", starter, "is", result[0], "and has a value", result[1])

if __name__ == '__main__':
    main()
    