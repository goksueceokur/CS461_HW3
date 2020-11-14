def Minimax(depth, breadt, starter, userInput):
    if starter== "minimizer":
        opponent = "maximizer"
    
    else:
        opponent = "minimizer"

    List = userInput
    j= depth

    while j != 0:
        if j%2 ==0:
            player= opponent
    
        else:
            player = starter

        while len(List) != breadt** (j-1):
            group =[]
            n= breadt

            while n != 0:
                group.append(List[0])
                List.remove(List[0])
                n= n-1

            if player == "maximizer":
                maxi= group[0]

                for k in group:
                    maxi = max( maxi, k)
                List.append(maxi)
                
            else:
                mini = group[0]
                for k in group:
                    mini = min( mini, k)
                List.append(mini)
        j -=1

    print(List)


def takeInput():
    takenInput = input("give input: ")
    userInput = takenInput.split(" ")

    for i in userInput:
        i= int(i)

    Minimax(2, 3, "maximizer", userInput)

takeInput()