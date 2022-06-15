
#wwtpn = [elevation, flowrate(m3/s), population, and base cost] based on sd wwtp data - this data is temporary as an input data - will be integrated with the spf algorthm if the nodes is already brokedown
wwtp_sd1 = [497, 0.005, 4066, 10000]
wwtp_sd2 = [467, 0.006, 4156, 15000]


#hmax segment only from WWTP 1-2 [elev, dist 1-hmax, dist hmax-2, total dist] - this data is using the data for the segment. only for highest point
hmax_segment_sd12 = [497, 1000, 590, 1590]


#data of hydraulics coefficients - this data is a list of coefficient , will be integrated in excel
hydraulics_coeff = {
    manning_coeff: 0.013,
    ks: 0.0015,
    viscosity: 0.000001,
    gravity_coeff: 9.81,
    efficincy_pump: 0.8,
    water_density: 998.21
    }


#data for pipe price for each diameter in mm [50, 80, 100, 125, 150, 200, 250] - the data for the pipe price
pipe_price_per_diam = [227.1, 259.7, 291.1, 326.6, 361.6, 459.7, 529.2]


#sample route =
#example segment = sd1-sd2

#######################################################################################################################
#This is a python file that contains a list of functions to run the pumping decision-making algorithm after getting the result which contains list of path from Floyd-Warshall algorithm simulation
#Every function has codes which based on the algo concept sheet in the Excel file to make it easier to be tracked

#FUNCTIONS OF PUMPING ALGORITHM - represented inside the box with black dashed lines

#######################################################################################################################
#A. DECISION MAKING OF DETERMINING THE SYSTEM - PUMPING OR GRAVITY
#INPUT: Elevation of the starting WWTP, elevation of the highest point, and the destinated WWTP in the selected segment - study case sd1 and sd2

#A1
def calc_elev_diff_hstart_hmax(hstart, hmax):
    """function to calculate the elevation differences from the starting wwtp to the highest point of the segment"""

    elev_diff_hstart_hmax = hmax - hstart
    return elev_diff_hstart_hmax

#executable command for calling A1 function
#calc_elev_diff_hstart_hmax(wwtp_sd1[0],hmax_segment_sd12[0]) #still on progress to be changed by reading the excel file


#A2
def calc_elev_diff_hmax_hend(hmax, hend):
    """function to calculate the elevation differences from the highest point to the end WWTP of the segment"""

    elev_diff_hmax_hend = hmax - hend
    return elev_diff_hmax_hend

#executable command for calling A2
#calc_elev_diff_hmax_hend(hmax_segment_sd12[0], wwtp_sd2[0]) #still on progress to be changed by reading the excel file

#######################################################################################################################
#B. PUMPING ALGORITHM - SEGMENT: START WWTP - HIGHEST POINT | ORANGE BOXES

#B1
#input : excel of the highest point data (elevation, distance to, and cooridnates)
def calc_slope_to_hmax_with_pump(flowrateb):
    """function to calculate the slope between starting WWTP to the highest point of the segment"""

    slope_to_hmax_with_pump = (2.33 * 0.0001 * (flowrateb ** (-0.46)))
    return slope_to_hmax_with_pump

#executable command for calling B1
calc_slope_to_hmax_with_pump(wwtp_sd1[1])


#B2
#input : excel of the hydraulic coefficient
def calc_diameter_to_hmax_with_pump(flowrateb, manningb, slopeb):
    """function to calculate the slope between starting WWTP to the highest point of the segment"""

    diameter_to_hmax_with_pump = (((flowrateb * manningb) / (0.3117 * (slopeb ** 0.5))) ** 0.375)
    return diameter_to_hmax_with_pump

#executable command for calling B2
calc_diameter_to_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1]))


#B3
def calc_velo_to_hmax_with_pump(flowrateb, diameterb):
    """function to calculate and check the velocity in the pipe between starting WWTP to the highest point of the segment"""

    velo_to_hmax_with_pump = (flowrateb * 4) / (3.14 * (diameterb ** 2))
    return velo_to_hmax_with_pump

#executable command for calling B3
calc_velo_to_hmax_with_pump(wwtp_sd1[1], calc_diameter_to_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1])))


#B4
def calc_rey_to_hmax_with_pump(diameterb, velocityb, viscosityb):
    """function to calculate and check the velocity in the pipe between starting WWTP to the highest point of the segment"""

    rey_to_hmax_with_pump = (diameterb * velocityb / viscosityb)
    return rey_to_hmax_with_pump

#executable command for calling B4
calc_rey_to_hmax_with_pump(calc_diameter_from_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1])),\
                           calc_velo_to_hmax_with_pump(wwtp_sd1[1], calc_diameter_to_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1]))), \
                           hydraulics_coeff[2])


#B5
def calc_ksd_to_hmax_with_pump(ks, diameterb):
    """function to calculate and check the ks/D value in the pipe between starting WWTP to the highest point of the segment"""

    ksd_to_hmax_with_pump = ks / diameterb
    return ksd_to_hmax_with_pump

#executable command for calling B5
calc_ksd_to_hmax_with_pump(hydraulics_coeff[1], calc_diameter_to_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1])))


#B6
def frictloss_to_hmax_with_pump():
    """function to calculate the friction loss in the pipe between starting WWTP to the highest point of the segment"""

    frictloss_to_hmax_with_pump =
    return frictloss_to_hmax_with_pump

#executable command for calling B6
calc_frictloss_to_hmax_with_pump()


#B7
def calc_total_head_to_hmax_with_pump(frictionlossb, headb):
    """function to calculate the total head in the pipe from start wwtp to highest point"""

    total_head_to_hmax_with_pump = frictionlossb + headb
    return total_head_to_hmax_with_pump

#executable command for calling B7
calc_total_head_to_hmax_with_pump()


#B8
def calc_pump_pow_to_hmax_with_pump(waterdensity, gravity, totalhead, flowrate, efficiency):
    """function to calculate the pump power for segment from starting WWTP to the highest point of the segment in kWh"""

    pump_pow_to_hmax_with_pump = (((waterdensity * gravity * totalhead * flowrate) / efficiency) / 1000)
    return pump_pow_to_hmax_with_pump

#executable command for calling B8 - power in kWh
calc_pump_pow_to_hmax_with_pump(hydraulics_coeff[5], hydraulics_coeff[3], calc_total_head_to_hmax_with_pump(), wwtp_sd1[1], hydraulics_coeff[4])


#B9
def calc_pump_cost_to_hmax_with_pump(250):
    """function to calculate the price of the pump in segment from starting WWTP to the highest point"""

    pump_cost_to_hmax_with_pump = 250 #reference is still needed - browse more from local shop in palestine
    return pump_cost_to_hmax_with_pump

#executable command for calling B9
calc_pump_cost_to_hmax_with_pump()


#B10
def calc_pipe_const_cost_to_hmax_with_pump(distanceb, pipecostb):
    """function to calculate the construction cost of the pipeline for segment from WWTP start to the highest point"""

    pipe_const_cost_to_hmax_with_pump = distanceb * pipecostb
    return pipe_const_cost_to_hmax_with_pump

#executable command for calling B10
calc_pipe_const_cost_to_hmax_with_pump()


#B11
def calc_manhole_to_hmax_with_pump(pipelength):
    """function to calculate the amount of manhole in the segment WWTP start to highest point"""
    # number of the manhole should be based on a valid literature or based on the qgis routing

    return pipelength / 50

#executable command for calling B11
calc_manhole_to_hmax_with_pump()


#B12
def calc_manhole_const_cost_to_hmax_with_pump(pricepermanholeb, numberofmanholeb):
    """function to calculate the construction cost of manholes in segment WWTP start to highest point"""
    #price of manhole construction - browse more on the palestine data and input as excel

    manhole_const_cost_to_hmax_with_pump = numberofmanholeb * pricepermanholeb
    return manhole_const_cost_to_hmax_with_pump

#executable command for calling B12
calc_manhole_const_cost_to_hmax_with_pump(x, calc_manhole_to_hmax_with_pump())


#B13
def calc_oper_main_cost_to_hmax_with_pump(powerpumpb, cost_per_hour, electricity_cost, run_hours):
    """function to calculate the cost of operational and maintenance in segment from WWTP start to the highest point with pump"""

    oper_main_cost_to_hmax_with_pump = ((powerpumpb * cost_per_hour * run_hours) + electricity_cost)
    return oper_main_cost_to_hmax_with_pump

#executable command for calling B13
calc_oper_main_cost_to_hmax_with_pump()


#B14
def calc_pump_station_cost_to_hmax_with_pump():
    """function to calculate the cost of pump station on segment start WWTP to highest point"""

    pump_station_cost_to_hmax_with_pump =   ##lit rev more on wwtp to pumping station - ask peter
    return pump_station_cost_to_hmax_with_pump

#executable command for calling B14
calc_pump_station_cost_to_hmax_with_pump()




#executable command for calling B15
calc_total_const_cost_to_hmax_with_pump()


#######################################################################################################################
#C. PUMPING ALGORITHM - SEGMENT: HIGHEST POINT - ENDING WWTP | YELLOW BOXES


#C1
def calc_slope_from_hmax_with_pump(flowratec):
    """function to calculate the elevation differences from the highest point to the ending wwtp of the segment"""

    slope_from_hmax_with_pump = (2.33 * flowratec * (0.134 ** (-0.46)))
    return slope_from_hmax_with_pump

#executable command for calling C1
calc_slope_from_hmax_with_pump(wwtp_sd1[1])


#C2
def calc_diameter_from_hmax_wwith_pump(flowratec, manningc, slopec):
    """function to calculate the diameter of the pipe on segment between the highest point to the ending wwtp"""

    diameter_from_hmax_with_pump = (((flowratec * manningc) / (0.3117 * (slopec ** 0.5))) ** 0.375)
    return diameter_from_hmax_with_pump

#executable command for calling C2
calc_diameter_from_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1]))


#C3
def calc_velo_from_hmax_with_pump(flowratec, diameterc):
    """function to calculate and check the velocity in the pipe between starting wwtp to highest point of the segment"""

    velo_from_hmax_with_pump = (flowratec * 4) / (3.14 * (diameterc ** 2))
    return velo_from_hmax_with_pump

#executable command for calling C3
calc_velo_from_hmax_with_pump(wwtp_sd1[1], calc_diameter_to_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1])))


#C4
def calc_rey_from_hmax_with_pump(diameterc, velocityc, viscosityc):
    """function to calculate and check the velocity in the pipe between starting wwtp to highest point of the segment"""

    rey_from_hmax_with_pump = (diameterc * velocityc / viscosityc)

    return rey_from_hmax_with_pump

calc_rey_from_hmax_with_pump(calc_diameter_from_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1])),\
                           calc_velo_to_hmax_with_pump(wwtp_sd1[1], calc_diameter_to_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1]))), \
                           hydraulics_coeff[2])


#C5
def calc_ksd_from_hmax_with_pump(ks, diameterc):
    """function to calculate and check the ks/D value in the pipe between the highest point to the ending wwtp of the segment"""

    ksd_from_hmax_with_pump = ks / diameterc
    return ksd_from_hmax_with_pump

calc_ksd_from_hmax_with_pump(hydraulics_coeff[1], calc_diameter_to_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1])))


#C6
def frictloss_from_hmax_with_pump():
    """function to calculate the friction loss inside the pipe between the highest point to the ending wwtp of the segment"""

    frictloss_from_hmax_with_pump = 0.05
    return frictloss_from_hmax_with_pump

calc_frictloss_from_hmax_with_pump()


#C7
def calc_total_head_from_hmax_with_pump(frictionlossc, headc):
    """function to calculate the total head in the pipe from the highest point to ending wwtp"""

    total_head_from_hmax_with_pump = frictionlossc + headc
    return total_head_from_hmax_with_pump

calc_total_head_from_hmax_with_pump()


#C8
def calc_pump_pow_from_hmax_with_pump(waterdensity, gravity, totalheadc, flowratec, efficiency):
    """function to calculate the power of the pump for segment of the highest point to the ending wwtp"""
    pump_pow_from_hmax_with_pump = ((waterdensity * gravity * totalheadc * flowratec) / efficiency)
    return pump_pow_from_hmax_with_pump

calc_pump_pow_from_hmax_with_pump(hydraulics_coeff[5], hydraulics_coeff[3], calc_total_head_to_hmax_with_pump(), wwtp_sd1[1], hydraulics_coeff[4])


#C9
def calc_pump_cost_from_hmax_with_pump():
    """function to calculate the price of the pump in segment from starting wwtp to highest point"""

    pump_cost_from_hmax_with_pump =
    return pump_cost_from_hmax_with_pump

calc_pump_cost_from_hmax_with_pump()


#C10
def calc_pipe_const_cost_from_hmax_with_pump():
    """function to calculate the construction cost of the pipeline for segment from the highest point to the ending wwtp"""

    pipe_const_cost_from_hmax_with_pump =
    return pipe_const_cost_from_hmax_with_pump

calc_pipe_const_cost_from_hmax_with_pump()


#C11
def calc_manhole_from_hmax_with_pump(pipelengthc):
    """function to calculate the amount of manhole in the segment wwtp start to highest point"""

    return pipelengthc / 50

calc_manhole_from_hmax_with_pump(hmax_segment_sd12[2])


#C12
def calc_manhole_const_cost_from_hmax_with_pump(pricepermanholec, numberofmanholec):
    """function to calculate the construction cost of manholes in segment from highest point to ending wwtp"""

    manhole_const_cost_from_hmax_with_pump = numberofmanholec * pricepermanholec
    return manhole_const_cost_from_hmax_with_pump

calc_manhole_const_cost_from_hmax_with_pump()


#C13
def calc_oper_main_cost_from_hmax_with_pump():
    """function to calculate the cost of operational and maintenance in segment from the highest point to ending WWTP with pump"""

    oper_main_cost_from_hmax_with_pump =
    return oper_main_cost_from_hmax_with_pump

calc_oper_main_cost_from_hmax_with_pump()


#C14
def calc_pump_station_cost_from_hmax_with_pump():
    """function to calculate the cost of the pumping station in segment the highest point to ending WWTP"""

    pump_station_cost_from_hmax_with_pump =
    return

calc_pump_station_cost_from_hmax_with_pump()


#######################################################################################################################
#D. PUMPING ALGORITHM - SEGMENT USING GRAVITY | PURPLE BOXES - need more breakdown

#D1
def calc_slope_segment_gravity(flowrated):
    """function to calculate the elevation differences from the highest point to the ending wwtp of the segment"""

    slope_segment_gravityp = (2.33 * flowrated * (0.134 ** (-0.46)))
    return slope_segment_gravity

#executable command for calling C1
calc_slope_segment_gravity(wwtp_sd1[1])


#D2
def calc_diameter_segment_gravity(flowrated, manningd, sloped):
    """function to calculate the diameter of the pipe on segment between the highest point to the ending wwtp"""

    diameter_segment_gravity = (((flowrated * manningd) / (0.3117 * (sloped ** 0.5))) ** 0.375)
    return diameter_segment_gravity

#executable command for calling C2
calc_diameter_segment_gravity(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1]))


#D3
def calc_velo_segment_gravity(flowrated, diameterd):
    """function to calculate and check the velocity in the pipe between starting wwtp to highest point of the segment"""

    velo_segment_gravity = (flowrated * 4) / (3.14 * (diameterd ** 2))
    return velo_segment_gravity

#executable command for calling C3
calc_velo_segment_gravity(wwtp_sd1[1], calc_diameter_to_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1])))


#D4
def calc_rey_segment_gravity(diameterd, velocityd, viscosityd):
    """function to calculate and check the velocity in the pipe between starting wwtp to highest point of the segment"""

    rey_segment_gravity = (diameterd * velocityd / viscosityd)

    return rey_segment_gravity

calc_rey_from_hmax_with_pump(calc_diameter_from_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1])),\
                           calc_velo_to_hmax_with_pump(wwtp_sd1[1], calc_diameter_to_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1]))), \
                           hydraulics_coeff[2]) #need to minimise


#D5
def calc_ksd_segment_gravity(ks, diameterc):
    """function to calculate and check the ks/D value in the pipe between the highest point to the ending wwtp of the segment"""

    ksd_segment_gravity = ks / diameterc
    return ksd_segment_gravity

calc_ksd_segment_gravity(hydraulics_coeff[1], calc_diameter_to_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1])))


#D6
def frictloss_segment_gravity():
    """function to calculate the friction loss inside the pipe between the highest point to the ending wwtp of the segment"""

    frictloss_segment_gravity = 0.05
    return frictloss_segment_gravity

calc_frictloss_segment_gravity()


#D7
def calc_total_head_segment_gravity(frictionlossc, headc):
    """function to calculate the total head in the pipe from the highest point to ending wwtp"""

    total_head_segment_gravity = frictionlossc + headc
    return total_head_segment_gravity

calc_total_head_from_hmax_with_pump()


#D8
def calc_pipe_const_cost_segment_gravity():
    """function to calculate the construction cost of the pipeline for segment from the highest point to the ending wwtp"""

    pipe_const_cost_segment_gravity =
    return pipe_const_cost_segment_gravity

calc_pipe_const_cost_segment_gravity()

#D9
def calc_manhole_segment_gravity(pipelengthc):
    """function to calculate the amount of manhole in the segment wwtp start to highest point"""

    return pipelengthc / 50

calc_manhole_segment_gravity(hmax_segment_sd12[2])


#D10
def calc_manhole_const_cost_segment_gravity(pricepermanholed, numberofmanholed):
    """function to calculate the construction cost of manholes in segment from highest point to ending wwtp"""

    manhole_const_cost_segment_gravity = numberofmanholed * pricepermanholed
    return manhole_const_cost_segment_gravity

calc_manhole_const_cost_segment_gravity()


#D11
def calc_oper_main_cost_gravity():
    """function to calculate the cost of operational and maintenance in segment from the highest point to ending WWTP with pump"""

    oper_main_cost_gravity =
    return oper_main_cost_gravity

calc_oper_main_cost_gravity()


#########################################################################################################################
#E - PART OF CALCULATING THE TOTAL COST OF CONSTRUCTION AND OPERATIONAL MAINTENANCE

#E1
def calc_total_cons_and_oper_segment_with_pump():
    """function to calculate the total const of the construction and operational&maintenance from both segments with pumping b and c"""

    total_cons_and_oper_segment_with_pump = B9 + B10 + B12 + B13 + C9 + C10 + C12 + C13
    return total_cons_and_oper_segment_with_pump

calc_total_cons_and_oper_segment_with_pump()

#E2
def calc_total_cons_and_oper_segment_gravity():
    """function to calculate the total const of the construction and operational&maintenance from segments with gravity"""

    total_cons_and_oper_segment_gravity = D8 + D10 + D11
    return total_cons_and_oper_segment_gravity

calc_total_cons_and_oper_segment_gravity()


#E3
def calc_grand_total_cost():
    """function to calculate the total const of the construction and operational&maintenance from both segments"""

    grand_total_cost = E1 + E2 + E3
    return grand_total_cost

calc_total_cons_and_oper_segment_gravity()


#####################################################################################################################
#list of command to execute the algorithm

#input:
#B
b1 = calc_slope_to_hmax_with_pump()
b2 = calc_diameter_segment_gravity()
b3 = calc_velo_to_hmax_with_pump()
b4 = calc_rey_to_hmax_with_pump()
b5 = calc_ksd_to_hmax_with_pump()
b6 = frictloss_to_hmax_with_pump()
b7 = calc_total_head_to_hmax_with_pump()
b8 = calc_pump_pow_to_hmax_with_pump()
b9 = calc_pump_cost_to_hmax_with_pump()
b10 = calc_pipe_const_cost_to_hmax_with_pump()
b11 = calc_manhole_to_hmax_with_pump()
b12 = calc_manhole_const_cost_to_hmax_with_pump()
b13 = calc_oper_main_cost_to_hmax_with_pump()
b14 = calc_pump_station_cost_to_hmax_with_pump()

#C
c1 = calc_slope_from_hmax_with_pump()
c2 = calc_diameter_from_hmax_wwith_pump()
c3 = calc_velo_from_hmax_with_pump()
c4 = calc_rey_from_hmax_with_pump()
c5 = calc_ksd_from_hmax_with_pump()
c6 = frictloss_from_hmax_with_pump()
c7 = calc_total_head_from_hmax_with_pump()
c8 = calc_pump_pow_from_hmax_with_pump()
c9 = calc_pump_cost_from_hmax_with_pump()
c10 = calc_pipe_const_cost_from_hmax_with_pump()
c11 = calc_manhole_from_hmax_with_pump()
c12 = calc_manhole_const_cost_from_hmax_with_pump()
c13 = calc_oper_main_cost_from_hmax_with_pump()
c14 = calc_pump_station_cost_from_hmax_with_pump()

#D
d1 = calc_slope_segment_gravity()
d2 = calc_diameter_segment_gravity()
d3 = calc_velo_segment_gravity()
d4 = calc_rey_segment_gravity()
d5 = calc_ksd_segment_gravity()
d6 = frictloss_segment_gravity()
d7 = calc_total_head_segment_gravity()
d8 = calc_pipe_const_cost_segment_gravity()
d9 = calc_manhole_segment_gravity()
d10 = calc_manhole_const_cost_segment_gravity()
d11 = calc_oper_main_cost_gravity()


#executions:
# #1. calculate the elevation difference for segment start WWTP to the highest point
elev_a1 = calc_elev_diff_hstart_hmax(wwtp_sd1[0], hmax_segment_sd12[0])
print(elev_a0)

elev_a2 = calc_elev_diff_hmax_hend()
print(elev_a2)

#2. decision making the value of a1 and a2, if it is more than 0, execute B or C, if below 0, execute D
if elev_a1 > 0:
    print(b1)
    print(b2)
    print(b3)
    print(b4)
    print(b5)
    print(b6)
    print(b7)
    print(b8)
    print(b9)
    print(b10)
    print(b11)
    print(b12)
    print(b13)
    print(b14)
else:
    print(d1)

if elev_a2 > 0:
    print(c1)
    print(c2)
    print(c3)
    print(c4)
    print(c5)
    print(c6)
    print(c7)
    print(c8)
    print(c9)
    print(c10)
    print(c11)
    print(c12)
    print(c13)
    print(c14)
else:
    print(d1)

#for part gravity (D), i just realised that I have to consider the gravity settings - still checking and doing it

e1 = calc_total_cons_and_oper_segment_with_pump()
e2 = calc_total_cons_and_oper_segment_gravity()

#calculating the grand total
e3 = e1 + e2

if e3 < #price of selected old wwtp :




































