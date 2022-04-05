
#wwtpn = [elevation, flowrate(m3/s), population, and base cost] based on sd wwtp data
wwtp_sd1 = [497, 0.005, 4066, 10000]
wwtp_sd2 = [467, 0.006, 4156, 15000]


#hmax segment only from WWTP 1-2 [elev, dist 1-hmax, dist hmax-2, total dist]
hmax_segment_sd12 = [497, 1000, 590, 1590]


#data of hydraulics coefficients
hydraulics_coeff = {
    manning_coeff: 0.013,
    ks: 0.0015,
    viscosity: 0.000001,
    gravity_coeff: 9.81,
    efficincy_pump: 0.8,
    water_density: 1000
    }


#data for pipe price for each diameter in mm [50, 80, 100, 125, 150, 200, 250]
pipe_price_per_diam = [227.1, 259.7, 291.1, 326.6, 361.6, 459.7, 529.2]


#sample route = wwtp 1 - wwtp 2 - wwtp
#example segment = sd1-sd2

#######################################################################################################################
#This is a python file that contains a list of functions to run the pumping decision-making algorithm
#Every function has codes which based on the algo concept sheet in the Excel file

#FUNCTIONS OF PUMPING ALGORITHM - represented inside the box with black dashed lines


#A0
def calc_elev_diff_wwtpend_wwtpstart(hend, hstart):
    """function to calculate the elevation differences between the selected wwtp from the list"""

    elev_diff_wwtpend_wwtpstart = hend - hstart
    return elev_diff_wwtpend_wwtpstart

calc_elev_diff_wwtpend_wwtpstart(wwtp_sd2[0],wwtp_sd1[0])


#A. PART OF PUMPING - GREEN BOXES

#A1
def calc_elev_diff_hstart_hmax(hstart, hmax):
    """function to calculate the elevation differences from the starting wwtp to the highest point of the segment"""

    elev_diff_hstart_hmax = hmax - hstart
    return elev_diff_hstart_hmax

calc_elev_diff_hstart_hmax(wwtp_sd1[0],hmax_segment_sd12[0])


#A2
def calc_elev_diff_hmax_hend(hmax, hend):
    """function to calculate the elevation differences from the highest point to
    the end wwtp of the segment"""

    elev_diff_hmax_hend = hmax - hend
    return elev_diff_hmax_hend

calc_elev_diff_hmax_hend(hmax_segment_sd12[0], wwtp_sd2[0])


#B. PUMPING ALGORITHM - SEGMENT: START WWTP - HMAX

#B1
def calc_slope_to_hmax_with_pump(flowrateb):
    """function to calculate the slope between starting wwtp to highest point of the segment"""

    slope_to_hmax_with_pump = (2.33 * 0.0001 * (flowrateb ** (-0.46)))
    return slope_to_hmax_with_pump

calc_slope_to_hmax_with_pump(wwtp_sd1[1])


#B2
def calc_diameter_to_hmax_with_pump(flowrateb, manningb, slopeb):
    """function to calculate the slope between starting wwtp to highest point of the segment"""

    diameter_to_hmax_with_pump = (((flowrateb * manningb) / (0.3117 * (slopeb ** 0.5))) ** 0.375)

    return diameter_to_hmax_with_pump

calc_diameter_to_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1]))



#B3
def calc_velo_to_hmax_with_pump(flowrateb, diameterb):
    """function to calculate and check the velocity in the pipe
    between starting wwtp to highest point of the segment"""

    velo_to_hmax_with_pump = (flowrateb * 4) / (3.14 * (diameterb ** 2))

    return velo_to_hmax_with_pump

calc_velo_to_hmax_with_pump(wwtp_sd1[1], calc_diameter_to_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1])))


#B4
def calc_rey_to_hmax_with_pump(diameterb, velocityb, viscosityb):
    """function to calculate and check the velocity in the pipe between starting wwtp to highest point of the segment"""

    rey_to_hmax_with_pump = (diameterb * velocityb / viscosityb)

    return rey_to_hmax_with_pump

calc_rey_to_hmax_with_pump(calc_diameter_from_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1])),\
                           calc_velo_to_hmax_with_pump(wwtp_sd1[1], calc_diameter_to_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1]))), \
                           hydraulics_coeff[2])


#B5
def calc_ksd_to_hmax_with_pump(ks, diameterb):
    """function to calculate and check the ks/D value in the pipe between starting wwtp to highest point of the segment"""

    ksd_to_hmax_with_pump = ks / diameterb

    return ksd_to_hmax_with_pump

calc_ksd_to_hmax_with_pump(hydraulics_coeff[1], calc_diameter_to_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1])))


#B6
def frictloss_to_hmax_with_pump():
    """function to calculate the friction loss in the pipe between starting wwtp to highest point of the segment"""

    frictloss_to_hmax_with_pump = 0.05
    return frictloss_to_hmax_with_pump

calc_frictloss_to_hmax_with_pump()



#B7
def calc_total_head_to_hmax_with_pump(frictionlossb, headb):
    """function to calculate the total head in the pipe from start wwtp to highest point"""

    total_head_to_hmax_with_pump = frictionlossb + headb
    return total_head_to_hmax_with_pump

calc_total_head_to_hmax_with_pump()


#B8
def calc_pump_pow_to_hmax_with_pump(waterdensity, gravity, totalhead, flowrate, efficiency):
    pump_pow_to_hmax_with_pump = ((waterdensity * gravity * totalhead * flowrate) / efficiency)
    return pump_pow_to_hmax_with_pump

calc_pump_pow_to_hmax_with_pump(hydraulics_coeff[5], hydraulics_coeff[3], calc_total_head_to_hmax_with_pump(), wwtp_sd1[1], hydraulics_coeff[4])


#B9
def calc_pump_cost_to_hmax_with_pump():
    """function to calculate the price of the pump in segment from starting wwtp to highest point"""

    pump_cost_to_hmax_with_pump =
    return pump_cost_to_hmax_with_pump

calc_pump_cost_to_hmax_with_pump()



#B10
def calc_pipe_const_cost_to_hmax_with_pump():
    """function to calculate the construction cost of the pipeline for segment from wwtp start to highest point"""

    pipe_const_cost_to_hmax_with_pump =
    return pipe_const_cost_to_hmax_with_pump

calc_pipe_const_cost_to_hmax_with_pump()


#B11
def calc_manhole_to_hmax_with_pump(pipelength):
    """function to calculate the amount of manhole in the segment wwtp start to highest point"""

    return pipelength / 50

calc_manhole_to_hmax_with_pump()


#B12
def calc_manhole_const_cost_to_hmax_with_pump(pricepermanholeb, numberofmanholeb):
    """function to calculate the construction cost of manholes in segment wwtp start to highest point"""

    manhole_const_cost_to_hmax_with_pump = numberofmanholeb * pricepermanholeb
    return manhole_const_cost_to_hmax_with_pump

calc_manhole_const_cost_to_hmax_with_pump()


#B13
def calc_oper_main_cost_to_hmax_with_pump():
    """function to calculate the cost of operational and maintenance in segment from wwtp start to
    highest point with pump"""

    oper_main_cost_to_hmax_with_pump =
    return oper_main_cost_to_hmax_with_pump

calc_oper_main_cost_to_hmax_with_pump()


#B14
def calc_pump_station_cost_to_hmax_with_pump():
    """function to calculate the cost of pump station on segment start wwtp to highest point"""

    pump_station_cost_to_hmax_with_pump =
    return pump_station_cost_to_hmax_with_pump

calc_pump_station_cost_to_hmax_with_pump()


#C. PUMPING ALGORITHM - SEGMENT: HMAX - ENDING WWTP

#C1
def calc_slope_from_hmax_with_pump(flowratec):
    """function to calculate the elevation differences from the highest point to the ending wwtp of the segment"""

    slope_from_hmax_with_pump = (2.33 * flowratec * (0.134 ** (-0.46)))
    return slope_from_hmax_with_pump

calc_slope_from_hmax_with_pump(wwtp_sd1[1])


#C2
def calc_diameter_from_hmax_wwith_pump(flowratec, manningc, slopec):
    """function to calculate the diameter of the pipe on segment between the highest point to the ending wwtp"""

    diameter_from_hmax_with_pump = (((flowratec * manningc) / (0.3117 * (slopec ** 0.5))) ** 0.375)
    return diameter_from_hmax_with_pump

calc_diameter_from_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1]))


#C3
def calc_velo_from_hmax_with_pump(flowratec, diameterc):
    """function to calculate and check the velocity in the pipe between starting wwtp to highest point of the segment"""

    velo_from_hmax_with_pump = (flowratec * 4) / (3.14 * (diameterc ** 2))

    return velo_from_hmax_with_pump

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
    """function to calculate the cost of operational and maintenance in segment from highest point to ending wwtp with pump"""

    oper_main_cost_from_hmax_with_pump =
    return oper_main_cost_from_hmax_with_pump

calc_oper_main_cost_from_hmax_with_pump()


#C14
def calc_pump_station_cost_from_hmax_with_pump():
    """function to calculate the cost of the pumping station in segment highest point to ending wwtp"""


#MAIN COMMAND FOR RUNNING THE DECISION-MAKING PUMPING ALGORITHM

#1. calculate the elevation difference (A0)
elev_a0 = calc_elev_diff_wwtpend_wwtpstart(wwtp_sd2[0],wwtp_sd1[0])
print(elev_a0)

if elev_a0 > 0:
    elev_a1

#2. calculate the elevation difference for each segment
elev_a1 = calc_elev_diff_hstart_hmax(wwtp_sd1[0],hmax_segment_sd12[0])
elev_a2 =


#2. If elevation is negative, then use gravity, otherwise use pump
if elev_a0 > 0: #if hend-hstart is positive, calculate hmax-hstart segment
    elev_a1
elif elev_a0 > 0: #if hend-start is positive, calculate hmax-hend segment
    elev_a2
else:
    #command to run the gravity calculation
    head = calc_elev_diff_hstart_hmax(wwtp_sd1[0], hmax_segment_sd12)
    slope = calc_slope_to_hmax_with_pump(wwwtp_sd1[1])



#data
    manning_coeff = 0.013
    ks = 0.0015
    viscosity = 0.000001
    gravity_coeff = 9.81
    efficincy_pump = 0.8
    water_density = 1000

    diam = calc_diameter_to_hmax_with_pumping(wwtp_sd1[1], manning_coeff, calc_slope_to_hmax_with_pump(wwtp_sd1[1]))
    vel = calc_velo_from_hmax_with_pump(wwtp_sd1[1], calc_diameter_from_hmax_with_pump(wwtp_sd2[1], manning_coeff, calc_slope_from_hmax_with_pump(wwtp_sd2[1])))
    reynolds = calc_reynold_to_hmax_with_pump(calc_diameter_from_hmax_with_pump())







































#function to calculate the manhole in the pipe by assuming every 50 m should be 1 manhole

distance_segment = [1590, 3736, 3281, 8006]

def calc_manhole_segment_without_pumping():
    manhole_segment_without_pumping = distance_segment[0] / 50
    return manhole_segment_without_pumping




#function to calculate the construction cost of pipe segment without pumping
#data of price of each diameter in ILS [50, 80, 100, 125, 150, 200, 250]



def calc_construct_cost_pipe_segment_without_pumping():
    construct_cost_pipe_segment_without_pumping = pipe_price_per_diam[5] * calc_diameter_segment_without_pumping()
    return construct_cost_pipe_segment_without_pumping





