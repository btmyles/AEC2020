
def configComp(map):
    #call jakob for each configuration
    configs = [[1,1], [1,2], [1,3,3], [1,2,3], [2,2,2], [2,3,3,3], [3,3,3,3]]
    minCost = -1
    minRed = -1
    bestConfig = -1
    for i in configs:
        (tempCost,tempRed) = minMax(map, configs)
        if minCost == -1 or minRed == -1:
            minCost = tempCost
            minRed = tempRed
            bestConfig = i
        elif tempCost < minCost:
            minCost = tempCost
            minRed = tempRed
            bestConfig = i
        elif tempCost == minCost:
            if tempRed < minRed:
                minRed = tempRed
                bestConfig = i