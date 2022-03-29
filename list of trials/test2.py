
#some hints from leo

#wwtp1 = [x, y, z, flor_R, cost]
#wwtp2 = [x, y, z, flor_R, cost]
#wwtp3 = [x, y, z, flor_R, cost]


wwtp1 = [25.2, 30.2, 10, 4, 7.5]
wwtp2 = [28.2, 39.2, 8, 4, 7.5]
wwtp3 = [35.2, 20.2, 12, 4, 7.5]

baseline_cost = wwtp1[4] + wwtp2[4] + wwtp3[4]


def cost_connecting_2(wwtp1, wwtp2):
    dist = calc_dist(wwtp1[0], wwtp1[1], wwtp2[0], wwtp[1])
    diam = calc_diameter(manning, slope, ...)
    c = cost_pipe(dist,diam, ...)
    return c

#------
def calc_dist(x1, y1, x2, y2):
    d = np.sqrt((y1-y2)**2 + (x1-x2)**2)
    return d

def calc_diameter(m, s, )
    diam = xxxx
    return diam

def cost_pipe(dist, diam)

tp = [wwtp1, wwtp2, wwtp3, wwtp4]
cost = []
for p1 in tp:
    for p2 in tp:
        cost.append = cost_connecting_2(p1,p2)

tp = [wwtp1, wwtp2, wwtp3, wwtp4]
cost = []
for p1 in tp:
    for p2 in tp:
        for p3 in tp:
            cost.append = cost_connecting_2(p1, p2)



#select 3 plants randomly from the list
random()