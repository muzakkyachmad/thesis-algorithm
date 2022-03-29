#wwtpn = [elevation, flowrate(m3/s), population, and base cost] based on sd wwtp data

wwtp_sd1 = [497, 0.005, 4066, 10000]
wwtp_sd2 = [467, 0.006, 4156, 15000]

hmax_segment_sd12 = 497 #hmax segment only from WWTP 1-2


#example route = sd1-sd2

#1. PART OF PUMPING ALGORITHM

#functions to calculate the elevation difference between selected wwtp
def calc_elev_diff_wwtpend_wwtpstart(hend, hstart):

    elev_diff_wwtpend_wwtpstart = hend - hstart
    #print(elev_diff_wwtpend_wwtpstart)

    return elev_diff_wwtpend_wwtpstart

#calc_elev_diff_wwtpend_wwtpstart(wwtp_sd2[0],wwtp_sd1[0])



#A. PART OF PUMPING


def calc_elev_diff_hstart_hmax(hstart, hmax):

    elev_diff_hstart_hmax = hmax - hstart
    #print(elev_diff_hstart_hmax)

    return elev_diff_hstart_hmax

#calc_elev_diff_hstart_hmax(wwtp_sd1[0],hmax_segment_sd12)



def calc_elev_diff_hmax_hend(hmax, hend):
    elev_diff_hmax_hend = hmax - hend
    print(elev_diff_hmax_hend)

    return elev_diff_hmax_hend

calc_elev_diff_hmax_hend(hmax_segment_sd12, wwtp_sd2[0])



def calc_slope_to_hmax_with_pump(flowrate):
    slope_to_hmax_with_pump = (2.33 * flowrate * (0.134 ** (-0.46)))
    #print(slope_to_hmax_with_pump)
    return slope_to_hmax_with_pump

#calc_slope_to_hmax_with_pump(wwwtp_sd1[1])


def calc_diameter_to_hmax_with_pumping(flowrate, manning, slope):
    diameter_to_hmax_with_pumping = (((flowrate * manning) / (0.3117 * (slope ** 0.5))) ** 0.375)
    #print(diameter_to_hmax_with_pumping)
    return diameter_to_hmax_with_pumping



def calc_slope_from_hmax_with_pump(flowrate):
    slope_from_hmax_with_pump = (2.33 * flowrate * (0.134 ** (-0.46)))
    print(slope_from_hmax_with_pump)
    return slope_from_hmax_with_pump

calc_slope_from_hmax_with_pump(wwtp_sd2[1])


def calc_diameter_from_hmax_with_pump(flowrate, manning, slope):
    diam_pipe_to_hmax_with_pump = (((flowrate * manning) / (0.3117 * (slope ** 0.5))) ** 0.375)
    print(diam_pipe_to_hmax_with_pump)
    return diam_pipe_to_hmax_with_pump

calc_diameter_to_hmax_with_pumping(wwtp_sd2[1], manning_coeff, calc_slope_from_hmax_with_pump(wwtp_sd2[1]))


def calc_velo_from_hmax_with_pump(flowrate, diameter):

    velo_from_hmax_with_pump = (flowrate * 4) / (3.14 * (diameter ** 2))
    #print(velo_from_hmax_with_pump)
    return velo_from_hmax_with_pump

#calc_velo_from_hmax_with_pump(wwtp_sd1[1], calc_diameter_from_hmax_with_pump(wwtp_sd2[1], manning_coeff, calc_slope_from_hmax_with_pump(wwtp_sd2[1]))

def calc_reynold_to_hmax_with_pump(diameter, viscosity, velocity):
    reynold_to_hmax_with_pump = (diameter * velocity / viscosity)

    return reynold_to_hmax_with_pump

#calc_reynold_to_hmax_with_pump(calc_diameter_from_hmax_with_pump())

def calc_ksd_to_hmax_with_pump():
    ksd_to_hmax_with_pump = ks / calc_diameter_segment_without_pumping()
    return ksd_to_hmax_with_pump

calc_ksd_to_hmax_with_pump()


# MAIN PROGRAMME
#1. Calculate elevation difference
elev = calc_elev_diff_wwtpend_wwtpstart(wwtp_sd2[0],wwtp_sd1[0])


#2. If elevation is negative, then use gravity, otherwise use pump
if elev < 0:
    #code for gravity

else:
    #code for pump
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


