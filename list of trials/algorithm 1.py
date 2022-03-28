#data of the wwtp - structure wwtpn = [elevation, flowrate(m3/s), population, and base cost] based on sd wwtp data

wwtp_sd1 = [497, 0.005, 4066, 10000]
wwtp_sd2 = [467, 0.006, 4156, 15000]
wwtp_sd3 = [460, 0.002, 1129, 5000]
wwtp_sd4 = [330, 0.002, 1716, 5000]
wwtp_sd5 = [377, 0.012, 7036, 20000]
wwtp_sd6 = [383, 0.057, 45861, 100000]
wwtp_sd7 = [382, 0.035, 23281, 60000]


#route = ba
#1. PART OF PUMPING ALGORITHM
#functions to calculate the elevation difference between selected wwtp
def calc_elev_diff_wwtpend_wwtpstart(a, b):
    """ function to calculate the elevation differences between selected wwtp
    from the floyd-warshall algorithm running result"""

    elev_diff_wwtpend_wwtpstart = b - a
    print(elev_diff_wwtpend_wwtpstart)

wwtp_sd_elev = [497, 467, 460, 330, 377, 383, 382] #wwtpsd1,2,3,4,5,6,7

calc_elev_diff_wwtpend_wwtpstart(wwtp_sd_elev[1], wwtp_sd_elev[2])


#A. PART OF PUMPING

hmax_segment_sd = [497, 537, 600, 600, 600, 530, 530, 600, 524, 557, 390, 520, 530, 530, 572, 575]

#A1. calculating the elevation difference of starting wwtp and highest point with pumping
def calc_elev_diff_hstart_hmax():
    """calculate the elevation difference on segment between starting wwtp\
     to the highest point on the segment with pumping scenario"""

    elev_diff_hstart_hmax = hmax_segment_sd[0] - wwtp_sd1[0]
    return elev_diff_hstart_hmax

calc_elev_diff_wwtpend_wwtpstart(a,b)


#A2. calculating the elevation difference on segment between highest point and ending wwtp with pumping
def calc_elev_diff_hmax_hend():
    elev_diff_hmax_hend =
    return elev_diff_hmax_hend


#A3. calculating slope of segment start to hmax pump
def calc_slope_to_hmax_with_pump()
    slope_to_hmax_with_pump =
    return slope_to_hmax_with_pump


#A4. calculating the diameter with pumping
def calc_diameter_segment_with_pumping():
    diameter_pipe_segment_with_pumping =
    return diameter_pipe_segment_with_pumping


#A5. calculating slope of segment hmax to end with pump
def calc_slope_from_hmax_with_pump()
    slope_from_hmax_with_pump =
    return slope_from_hmax_with_pump

#A6. calculating the diameter of pipe segment to max with pump
def calc_pipe_diam_to_hmax_with_pump():
    diam_pipe_to_hmax_with_pump =
    return diam_pipe_to_hmax_with_pump

#A7. calculating the diameter of pipe segment from max with pump
def calc_pipe_diam_from_hmax_with_pump():
    diam_pipe_from_hmax_with_pump =
    return diam_pipe_from_hmax_with_pump

#A8. calculating the reynold number on pipe with pumping
def calc_reynold_of_pipe_in_segment_with_pumping():
    reynold_segment_with_pumping = ((calc_velocity_segment_without_pumping() * calc_diameter_segment_without_pumping()) / viscosity)
    return reynold_segment_with_pumping

#A9. calculating the ks/D on pipe with pumping
def calc_ksD_segment_with_pumping():
    ksD_segment_with_pumping = ks / calc_diameter_segment_without_pumping()
    return ksD_segment_with_pumping

#A10.



#A9. calculating the velocity of pipe segment to max with pump
def calc_velo_to_hmax_with_pump():
    velo_to_hmax_with_pump =
    return velo_to_hmax_with_pump

#A9. calculating the velocity of


#A7. calculating the velocity on the pressured pipe

#B. PART OF WITHOUT PUMPING

#functions to calculate the diameter on a segment without pumping
def calc_slope_to_hmax_wihout_pumping():
    slope_to_hmax_without_pump = (2.33 * wwtp_sd1[1] * (0.134 ** (-0.46)))
    return slope_to_hmax_without_pump



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





