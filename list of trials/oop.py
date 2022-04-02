

wwtp_sd1 = [497, 0.005, 4066, 10000]
wwtp_sd2 = [467, 0.006, 4156, 15000]

hmax_segment_sd12 = 497 #hmax segment only from WWTP 1-2


#example route = sd1-sd2

#1. PART OF PUMPING ALGORITHM

#functions to calculate the elevation difference between selected wwtp
def calc_elev_diff_wwtpend_wwtpstart(hend, hstart):
    return print(hend - hstart)

calc_elev_diff_wwtpend_wwtpstart(wwtp_sd2[0],wwtp_sd1[0])