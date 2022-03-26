#data of the wwtp - structure wwtpn = [elevation, flowrate(m3/s), population, and base cost] based on sd wwtp data

wwtp_sd1 = [497, 0.005, 4066, 10000]
wwtp_sd2 = [467, 0.006, 4156, 15000]
wwtp_sd3 = [460, 0.002, 1129, 5000]
wwtp_sd4 = [330, 0.002, 1716, 5000]
wwtp_sd5 = [377, 0.012, 7036, 20000]
wwtp_sd6 = [383, 0.057, 45861, 100000]
wwtp_sd7 = [382, 0.035, 23281, 60000]


#functions to calculate the elevation difference between selected wwtp
def calc_elev_diff_wwtpend_wwtpstart():
    elev_diff_wwtpend_wwtpstart = wwtp_sd1[0] - wwtp_sd2[0]
    if elev_diff_wwtpend_wwtpstart > 0:
        calc_elev_diff_hmax_start()
    else:
        calc_slope_to_hmax()
return elef_diff_wwtpend_wwtpstart


hmax_segment_sd = [497, 537, 600, 600, 600, 530, 530, 600, 524, 557, 390, 520, 530, 530, 572, 575]
#function to calculate the elevation difference with pumping
def calc_elev_diff_hmax_hstart():
    elev_diff_hmax_hstart = hmax_segment_sd[0] - wwtp_sd1[0]
    return elev_diff_hmax_hstart


#functions to calculate the diameter on a segment without pumping
def calc_slope_to_hmax():
    slope_to_hmax = (2.33 * wwtp_sd1[1] * (0.134 ** (-0.46)))
    return slope_to_hmax

#hydraulic coefficients

manning_coeff = 0.013
ks = 0.0015
viscosity = 0.000001
gravity_coeff = 9.81
efficincy_pump = 0.8
water_density = 1000

#functions to calculate the diameter if the segment is not using pumping
def calc_diameter_segment_without_pumping():
    diameter_segment_without_pumping = (((wwtp_sd1[1] * manning_coeff) / (0.3117 * (calc_slope_to_hmax() ** 0.5))) ** 0.375)
    return diameter_segment_without_pumping

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








#functions to calculate the diameter on a segment without pumping



