from algorithm import MinMax

def configComp(map):
    configs = [[1,1], [1,2], [1,3,3], [1,2,3], [2,2,2]]
    minCost = -1
    minRed = -1
    minArr = []
    for i in configs:
        tempCost,tempRed,tempArr = MinMax(map, i)
        print("found, ", i)
        if minCost == -1 or minRed == -1:
            minCost = tempCost
            minRed = tempRed
            minArr = tempArr
        elif tempCost < minCost:
            minCost = tempCost
            minRed = tempRed
            minArr = tempArr
        elif tempCost == minCost:
            if tempRed < minRed:
                minRed = tempRed
                minArr = tempArr
    return (minCost, minRed, minArr)
