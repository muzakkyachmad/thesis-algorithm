

def costsPrivateSewers(buildings, buildPoints, pipeDiameterPrivateSewer, averageTrenchDepthPrivateSewer, lifeSewers,
                       interestRate, operationCosts, fc_SewerCost):
    '''
    This function calculates the costs of the private sewers. The private sewers are the closest distance to the street network,
    If the street is too far, the whole distance to the building is used.

    Input:
    buildings                          -    Buildings
    buildPoints                        -    Coordinates of Buildings
    pipeDiameterPrivateSewer           -    Pipe Diameter
    averageTrenchDepthPrivateSewer     -    Average Trench depth
    lifeSewers                         -    Lifespan of sewers
    interestRate                       -    Interest rate
    operationCosts                     -    Opex
    fc_SewerCost                       -    cost factor sewers

    Output:
    totCostPrivateSewer                -    Total replacement value of private sewers
    '''
    costsP_Sewer = 0
    for node in buildings:
        pt_to1_X, pt_to1_Y, gebListe = node[0], node[1], node[2]

        for house in gebListe:
            for geb in buildPoints:
                if geb[0] == house:
                    _, pt_from1_X, pt_from1_Y, _ = geb[0], geb[1], geb[2], geb[4]
                    break

            p0, p1 = (pt_from1_X, pt_from1_Y), (pt_to1_X, pt_to1_Y)
            distance = math.hypot(p0[0] - p1[0], p0[1] - p1[1])

            privateSewercostsPerYear = calculatePipeCosts(pipeDiameterPrivateSewer, distance,
                                                          averageTrenchDepthPrivateSewer, lifeSewers, interestRate,
                                                          operationCosts, fc_SewerCost)
            costsP_Sewer += privateSewercostsPerYear

    totCostPrivateSewer = costsP_Sewer * lifeSewers
    return totCostPrivateSewer