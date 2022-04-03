
#wwtpn = [elevation, flowrate(m3/s), population, and base cost] based on sd wwtp data

wwtp_sd1 = [497, 0.005, 4066, 10000]
wwtp_sd2 = [467, 0.006, 4156, 15000]

hmax_segment_sd12 = 497 #hmax segment only from WWTP 1-2

#data
hydraulics_coeff = {
    manning_coeff: 0.013,
    ks: 0.0015,
    viscosity: 0.000001,
    gravity_coeff: 9.81,
    efficincy_pump: 0.8,
    water_density: 1000
    }


#example route = sd1-sd2


#######################################################################################################################

#This is a python file that contains a list of functions to run the pumping decision-making algorithm
#Every function has codes which based on the algo concept sheet in the Excel file


#PART OF PUMPING ALGORITHM - this algorithm will be represented in scheme under the black dashed box


#A0
def calc_elev_diff_wwtpend_wwtpstart(hend, hstart):
    """function to calculate the elevation differences between the selected wwtp of each segment"""

    elev_diff_wwtpend_wwtpstart = hend - hstart
    return elev_diff_wwtpend_wwtpstart

calc_elev_diff_wwtpend_wwtpstart(wwtp_sd2[0],wwtp_sd1[0])


#A. PART OF PUMPING - GREEN BOXES

#A1
def calc_elev_diff_hstart_hmax(hstart, hmax):
    """function to calculate the elevation differences from the starting wwtp
    to the highest point of the segment"""

    elev_diff_hstart_hmax = hmax - hstart
    return elev_diff_hstart_hmax

calc_elev_diff_hstart_hmax(wwtp_sd1[0],hmax_segment_sd12)


#A2
def calc_elev_diff_hmax_hend(hmax, hend):
    """function to calculate the elevation differences from the highest point to
    the end wwtp of the segment"""

    elev_diff_hmax_hend = hmax - hend
    return elev_diff_hmax_hend

calc_elev_diff_hmax_hend(hmax_segment_sd12, wwtp_sd2[0])


#B. PUMPING ALGORITHM - SEGMENT: START WWTP - HMAX

#B1
def calc_slope_to_hmax_with_pump(flowrate):
    """function to calculate the slope between starting wwtp to highest point of the segment"""

    slope_to_hmax_with_pump = (2.33 * 0.0001 * (flowrate ** (-0.46)))
    return slope_to_hmax_with_pump

calc_slope_to_hmax_with_pump(wwtp_sd1[1])


#B2
def calc_diameter_to_hmax_with_pump(flowrate, manning, slope):
    """function to calculate the slope between starting wwtp to highest point of the segment"""

    diameter_to_hmax_with_pump = (((flowrate * manning) / (0.3117 * (slope ** 0.5))) ** 0.375)

    return diameter_to_hmax_with_pump

calc_diameter_to_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1]))



#B3
def calc_velo_to_hmax_with_pump(flowrate, diameter):
    """function to calculate and check the velocity in the pipe
    between starting wwtp to highest point of the segment"""

    velo_to_hmax_with_pump = (flowrate * 4) / (3.14 * (diameter ** 2))

    return velo_to_hmax_with_pump

calc_velo_to_hmax_with_pump(wwtp_sd1[1], calc_diameter_to_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1])))


#B4
def calc_rey_to_hmax_with_pump(diameter, velocity, viscosity):
    """function to calculate and check the velocity in the pipe between
    starting wwtp to highest point of the segment"""

    rey_to_hmax_with_pump = (diameter * velocity / viscosity)

    return rey_to_hmax_with_pump

calc_rey_to_hmax_with_pump(calc_diameter_from_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1])),\
                           calc_velo_to_hmax_with_pump(wwtp_sd1[1], calc_diameter_to_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1]))), \
                           hydraulics_coeff[2])


#B5
def calc_ksd_to_hmax_with_pump(ks, diameter):
    """function to calculate and check the ks/D value in the pipe between
    starting wwtp to highest point of the segment"""

    ksd_to_hmax_with_pump = ks / diameter

    return ksd_to_hmax_with_pump

calc_ksd_to_hmax_with_pump(hydraulics_coeff[1], calc_diameter_to_hmax_with_pump(wwtp_sd1[1], hydraulics_coeff[0], calc_slope_to_hmax_with_pump(wwtp_sd1[1])))



#B6
def frictloss_to_hmax_with_pump():
    """function to calculate the friction loss in the pipe between
    starting wwtp to highest point of the segment"""

    frictloss_to_hmax_with_pump = 0.05

    return frictloss_to_hmax_with_pump

calc_frictloss_to_hmax_with_pump()



#B7
def calc_total_head_to_hmax_with_pump(frictionloss, head):
    """function to calculate the total head in the pipe from start wwtp to highest point"""

    total_head_to_hmax_with_pump = frictionloss + head
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
def calc_manhole_const_cost_to_hmax_with_pump(pricepermanhole, numberofmanhole):
    """function to calculate the construction cost of manholes in segment wwtp start to highest point"""

    manhole_const_cost_to_hmax_with_pump = numberofmanhole * pricepermanhole
    return manhole_const_cost_to_hmax_with_pump

calc_manhole_const_cost_to_hmax_with_pump()


#B13
def calc_oper_main_cost_to_hmax_with_pump():
    """function to calculate the cost of operational and maintenance in segment from wwtp start to
    highest point with pump"""

    oper_main_cost_to_hmax_with_pump =
    return oper_main_cost_to_hmax_with_pump

calc_oper_main_cost_to_hmax_with_pump()



#C. PUMPING ALGORITHM - SEGMENT: HMAX - ENDING WWTP

#C1
def calc_slope_from_hmax_with_pump(flowrate):
    slope_from_hmax_with_pump = (2.33 * flowrate * (0.134 ** (-0.46)))
    return slope_from_hmax_with_pump

calc_slope_from_hmax_with_pump(wwtp_sd1[1])


#C2
def calc_diameter_from_hmax_wwith_pump():




#hydraulic coefficients

hydraulics_coeff = {
    manning_coeff: 0.013,
    ks: 0.0015,
    viscosity: 0.000001,
    gravity_coeff: 9.81,
    efficincy_pump: 0.8,
    water_density: 1000
    }

#functions to calculate the diameter if the segment is not using pumping
def calc_diameter_segment_without_pumping():
    import manning_coeff from hydraulics_coeff

    diameter_segment_without_pumping = (((wwtp_sd1[1] * manning_coeff) / (0.3117 * (calc_slope_to_hmax() ** 0.5))) ** 0.375)

    return diameter_segment_without_pumping

calc_diameter_segment_without_pumping()



#functions to velocity of the pipe if the segment is not using pumping
def calc_velocity_segment_without_pumping():
    velocity_segment_without_pummping = ((wwtp_sd1[1] * 4) / (3.14 * (calc_diameter_segment_without_pumping() ** 2)))
    return velocity_segment_without_pummping




#functions to calculate reynold nunmber if the segment is not using pumping
def calc_reynold_segment_without_pumping():
    reynold_segment_without_pumping = ((calc_velocity_segment_without_pumping() * calc_diameter_segment_without_pumping()) / viscosity)
    return reynold_segment_without_pumping



#functions to calculate ks/D value if the segment is not using pumping
def calc_ksD_segment_without_pumping():
    ksD_segment_without_pumping = ks / calc_diameter_segment_without_pumping()
    return ksD_segment_without_pumping



#function to calculate the manhole in the pipe by assuming every 50 m should be 1 manhole

distance_segment = [1590, 3736, 3281, 8006]

def calc_manhole_segment_without_pumping():
    manhole_segment_without_pumping = distance_segment[0] / 50
    return manhole_segment_without_pumping




#function to calculate the construction cost of pipe segment without pumping
#data of price of each diameter in ILS [50, 80, 100, 125, 150, 200, 250]

pipe_price_per_diam = [227.1, 259.7, 291.1, 326.6, 361.6, 459.7, 529.2]

def calc_construct_cost_pipe_segment_without_pumping():
    construct_cost_pipe_segment_without_pumping = pipe_price_per_diam[5] * calc_diameter_segment_without_pumping()
    return construct_cost_pipe_segment_without_pumping





