



# 1. PART OF PUMPING ALGORITHM
# functions to calculate the elevation difference between selected wwtp
def calc_elev_diff_wwtpend_wwtpstart(a, b):
    """calculate the elevation difference between wwtp end and wwtp start"""

    elev_diff_wwtpend_wwtpstart = b - a
    print(elev_diff_wwtpend_wwtpstart)
    return elev_diff_wwtpend_wwtpstart

wwtp_sd_elev = [497, 467, 460, 330, 377, 383, 382]

calc_elev_diff_wwtpend_wwtpstart(wwtp_sd_elev[1],wwtp_sd_elev[2])

if calc_elev_diff_wwtpend_wwtpstart(wwtp_sd_elev[1],wwtp_sd_elev[2]) > 0:
    sa()
else:
    ya()
print(f"pumping")


def sa():
    return

def ya():
    print(f"no pump")
    return
