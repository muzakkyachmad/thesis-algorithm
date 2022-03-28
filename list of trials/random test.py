



# 1. PART OF PUMPING ALGORITHM
# functions to calculate the elevation difference between selected wwtp
def calc_elev_diff_wwtpend_wwtpstart(a, b):
    """calculate the elevation difference between wwtp end and wwtp start"""

    elev_diff_wwtpend_wwtpstart = b - a
    print(elev_diff_wwtpend_wwtpstart)


wwtp_sd_elev = [497, 467, 460, 330, 377, 383, 382]

calc_elev_diff_wwtpend_wwtpstart(wwtp_sd_elev[1],wwtp_sd_elev[2])






def calc_elev_diff_wwtpend_wwtpstart2(a, b):
    """calculate the elevation difference between wwtp end and wwtp start"""

    elev_diff_wwtpend_wwtpstart2 = b - a
    print(elev_diff_wwtpend_wwtpstart2)


wwtp_sd_elev2 = [497, 467, 460, 330, 377, 383, 382]

calc_elev_diff_wwtpend_wwtpstart(wwtp_sd_elev2[1],wwtp_sd_elev2[2])

