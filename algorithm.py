from copy import deepcopy

max = 1.75 * (10 ** 6)

reduc = 0.21

"""
CCS 1:
Central reduc -> 22.3%
Radius 1: 16.8%
Radius 2: 13.7%
Radius 3: 9.2%
Radius 4: 2.1%

Increases to 689 ppm for 2 months, then return
Initial Cost:   $683,732.76
Monthly Fee:    $12,297.32
-> 831300.6

CCS 2:
Central reduc ->17.2%
Radius 1: 13.9%
Radius 2: 5.3%

Increases to 531 ppm for 2 months, then return
Initial Cost:   $410,298.81
Monthly Fee:    $9,465.78
-> 523888.17 total

CCS 3
Central reduc -> 11.5%
Radius 1: 6.7%

Increases to 486 ppm for 1 month, then return
Initial Cost:   $410,298.81
Monthly Fee:    $9,465.78
-> 371918.55 total

"""

class CCS():
    def __init__(self, name, cost, radii, effective, increasedPPM, months):
        self.name = name
        self.cost = cost
        self.radii = radii          #Radiuses (array)
        self.effective = effective  #Effectivity of each radius (array)
        self.increasedPPM = increasedPPM
        self.months = months

    
    def __str__(self):
        return "{0}{1}".format("CCS", self.name)

def CCS1():
    return CCS("1", 831300.6, 4, [22.3, 16.8, 13.7, 9.2, 2.1], 689, 2)

def CCS2():
    return CCS("2", 523888.17, 2, [17.2, 13.9, 5.3], 531, 2)

def CCS3():
    return CCS("3", 371918.55, 1, [11.5, 6.7], 486, 1)

'''
ARRAY OF CCS to SET OF CCS
'''
def set_ccs(conf):
    used = []
    to_delete = []
    for item in conf:
        if item.name in used:
            to_delete.append(item)
        else:
            used.append(item.name)
    v = []
    for u in used:
        if u == '1':
            v.append(CCS1())
        elif u == '2':
            v.append(CCS2())
        elif u == '3':
            v.append(CCS3())

    return v

'''
brute force algorithm
'''
"""
def MinMax(PPMmap, conf, total_cost, co2_reduction, path):
    global List_of_best
    global checked
    print(len(conf))
    if len(conf) == 0:
        List_of_best.append(path)
        start = path[0]
        checked.append((start[0], start[1]))
        return
    for i in range(len(PPMmap)):
        row = i
        for j in range(len(PPMmap[0])):
            col = j
            if PPMmap[i][j][1] == 1 :
                if ((not path) and ((row, col) in checked)):
                    print("------>>>>>>>>>",row, col)
                    break
                reduc, dollas = place_node(PPMmap, row, col, conf[0])
                co2_reduction += reduc
                total_cost += dollas
                path.append((row,col, conf[0].name))
                print("RECUS", checked)
                MinMax(PPMmap, conf[1:], total_cost, co2_reduction, path)
"""
def MinMax(PPMmap, conf):
    #[2, 3]
    conf = num2CCS(conf)
    best = None
    indexes = -1
    valids = ValidNodes(PPMmap)

    if len(conf) == 2:
        for i in range(len(valids)):
            for j in range(len(valids)):
                if i != j:
                    PPMmap_c = deepcopy(PPMmap)
                    co2, cost = place_node(PPMmap_c, valids[i][0], valids[i][1], conf[0])
                    co22, cost2 = place_node(PPMmap_c, valids[j][0], valids[j][1], conf[1])

                    t_cost = cost + cost2
                    t_co2 = co2 + co22

                    if best == None or best[1] < t_co2:
                        best = (t_cost, t_co2)
                        indexes = [(valids[i][0], valids[i][1], conf[0].name), (valids[j][0], valids[j][1], conf[1].name)]


    elif len(conf) == 3:
        for i in range(len(valids)):
            for j in range(len(valids)):
                if i != j:
                    for k in range(len(valids)):
                        if k != j and k != i:
                            PPMmap_c = deepcopy(PPMmap)
                            co2, cost = place_node(PPMmap_c, valids[i][0], valids[i][1], conf[0])
                            co22, cost2 = place_node(PPMmap_c, valids[j][0], valids[j][1], conf[1])
                            co23, cost3 = place_node(PPMmap_c, valids[k][0], valids[k][1], conf[1])

                            t_cost = cost + cost2 + cost3
                            t_co2 = co2 + co22 + co23

                            if best == None or best[1] < t_co2:
                                best = (t_cost, t_co2)
                                indexes = [(valids[i][0], valids[i][1], conf[0].name), (valids[j][0], valids[j][1], conf[1].name), (valids[k][0], valids[k][1], conf[2].name)]



    elif len(conf) == 4:
        indexes = []
        for i in range(len(valids)):
            for j in range(len(valids)):
                if i != j:
                    for k in range(len(valids)):
                        if k != j and k != i:
                            for l in range(len(valids)):
                                if l != i and l != j and l != k:
                                    PPMmap_c = deepcopy(PPMmap)
                                    co2, cost = place_node(PPMmap_c, valids[i][0], valids[i][1], conf[0])
                                    co22, cost2 = place_node(PPMmap_c, valids[j][0], valids[j][1], conf[1])
                                    co23, cost3 = place_node(PPMmap_c, valids[k][0], valids[k][1], conf[1])
                                    co24, cost4 = place_node(PPMmap_c, valids[l][0], valids[l][1], conf[1])

                                    t_cost = cost + cost2 + cost3 + cost4
                                    t_co2 = co2 + co22 + co23 + co24

                                    if best == None or best[1] < t_co2:
                                        best = (t_cost, t_co2)
                                        indexes = [(valids[i][0], valids[i][1], conf[0].name), (valids[j][0], valids[j][1], conf[1].name), (valids[k][0], valids[k][1], conf[2].name), (valids[l][0], valids[l][1], conf[3].name)]

    return best[0], best[1], indexes

def ValidNodes(PPMmap):
    ret = []
    for i in range(len(PPMmap)):
        for j in range(len(PPMmap[0])):
            if PPMmap[i][j][1] == 1:
                ret.append((i, j))

    return ret

def place_node(PPMmap, row, col, elem):
    reduced_ppm = 0
    rows = len(PPMmap)
    cols = len(PPMmap[0])
    if elem.radii > 3:
        #UP 4
        if row - 4 >= 0:
            reduced_ppm += PPMmap[row - 4][col][0] * elem.effective[4]
        if row - 3 >= 0:
            if col - 1 >= 0:
                reduced_ppm += PPMmap[row-3][col-1][0] * elem.effective[4]
            if col + 1 < cols:
                reduced_ppm += PPMmap[row-3][col + 1][0] * elem.effective[4]
        if row - 2 >= 0:
            if col - 2 >= 0:
                reduced_ppm += PPMmap[row-2][col-2][0] * elem.effective[4]
            if col + 2 < cols:
                reduced_ppm += PPMmap[row-2][col + 2][0] * elem.effective[4]
        if row - 1 >= 0:
            if col - 3 >= 0:
                reduced_ppm += PPMmap[row-1][col-3][0] * elem.effective[4]
            if col + 3 < cols:
                reduced_ppm += PPMmap[row-1][col+3][0] * elem.effective[4]
        if row >= 0:
            if col - 4 >= 0:
                reduced_ppm += PPMmap[row][col-4][0] * elem.effective[4]
            if col + 4 < cols:
                reduced_ppm += PPMmap[row][col+4][0] * elem.effective[4]

        if row + 4 < rows:
            reduced_ppm += PPMmap[row + 4][col][0] * elem.effective[4]
        if row + 3 < rows:
            if col - 1 >= 0:
                reduced_ppm += PPMmap[row+3][col-1][0] * elem.effective[4]
            if col + 1 < cols:
                reduced_ppm += PPMmap[row+3][col + 1][0] * elem.effective[4]
        if row + 2 < rows:
            if col - 2 >= 0:
                reduced_ppm += PPMmap[row+2][col-2][0] * elem.effective[4]
            if col + 2 < cols:
                reduced_ppm += PPMmap[row+2][col + 2][0] * elem.effective[4]
        if row + 1 < rows:
            if col - 3 >= 0:
                reduced_ppm += PPMmap[row+1][col-3][0] * elem.effective[4]
            if col + 3 < cols:
                reduced_ppm += PPMmap[row+1][col+3][0] * elem.effective[4]

    if elem.radii > 2:
        if row - 3 >= 0:
            reduced_ppm += PPMmap[row-3][col][0] * elem.effective[3]
        if row - 2 >= 0:
            if col - 1 >= 0:
                reduced_ppm += PPMmap[row-2][col-1][0] * elem.effective[3]
            if col + 1 < cols:
                reduced_ppm += PPMmap[row-2][col+1][0] * elem.effective[3]
        if row - 1 >= 0:
            if col - 2 < cols:
                reduced_ppm += PPMmap[row-1][col-2][0] * elem.effective[3]
            if col + 2 < cols:
                reduced_ppm += PPMmap[row-1][col+2][0] * elem.effective[3]  
        if row  >= 0:
            if col - 3 >= 0:
                reduced_ppm += PPMmap[row][col-3][0] * elem.effective[3]
            if col + 3 < cols:
                reduced_ppm += PPMmap[row][col+3][0] * elem.effective[3]          
        
        if row + 3 < rows:
            reduced_ppm += PPMmap[row+3][col][0] * elem.effective[3]
        if row + 2 < rows:
            if col - 1 >= 0:
                reduced_ppm += PPMmap[row+2][col-1][0] * elem.effective[3]
            if col + 1 < cols:
                reduced_ppm += PPMmap[row+2][col+1][0] * elem.effective[3]
        if row + 1 < rows:
            if col - 2 >= 0:
                reduced_ppm += PPMmap[row+1][col-2][0] * elem.effective[3]
            if col + 2 < cols:
                reduced_ppm += PPMmap[row+1][col+2][0] * elem.effective[3]  
    if elem.radii > 1:
        if row - 2 >= 0:
            reduced_ppm += PPMmap[row-2][col][0] * elem.effective[2]
        if row - 1 >= 0:
            if col - 1 >= 0:
                reduced_ppm += PPMmap[row-1][col-1][0] * elem.effective[2]
            if col + 1 < cols:
                reduced_ppm += PPMmap[row-1][col + 1][0] * elem.effective[2]
        if row >= 0:
            if col - 2 >= 0:
                reduced_ppm += PPMmap[row][col - 2][0] * elem.effective[2]
            if col + 2 < cols:
                reduced_ppm += PPMmap[row][col + 2][0] * elem.effective[2]
        if row + 2 < rows:
            reduced_ppm += PPMmap[row+2][col][0] * elem.effective[2]
        if row + 1 < rows:
            if col - 1 >= 0:
                reduced_ppm += PPMmap[row+1][col-1][0] * elem.effective[2]
            if col + 1 < cols:
                reduced_ppm += PPMmap[row+1][col + 1][0] * elem.effective[2]

    if elem.radii > 0:
        if row - 1 >= 0:
            reduced_ppm += PPMmap[row-1][col][0] * elem.effective[1]
        if row >= 0:
            if col - 1 >= 0:
                reduced_ppm += PPMmap[row][col - 1][0] * elem.effective[1]
            if col + 1 < cols:
                reduced_ppm += PPMmap[row][col + 1][0] * elem.effective[1]
        if row + 1 < rows:
            reduced_ppm += PPMmap[row+1][col][0] * elem.effective[1]

    reduced_ppm *= 12/100
    reduced_ppm += PPMmap[row][col][0] * elem.effective[0]/100 * (12 - elem.months)

    reduced_ppm -= (elem.increasedPPM * elem.months)

    PPMmap[row][col] = (PPMmap[row][col][0], 0)

    return reduced_ppm, elem.cost

def num2CCS(conf):
    ret = []
    for elem in conf:
        if elem == 1:
            ret.append(CCS1())
        elif elem == 2:
            ret.append(CCS2())
        elif elem == 3:
            ret.append(CCS3())

        
    return ret

#READ_FILE: filename -> 2D-array



"""
for rows:
    for cols:
        if valid:
            place a CCS
            check reductions

"""



    

