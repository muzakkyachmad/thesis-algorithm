
import elevation in inputdatawwtp7sd


#A0
def calc_elev_diff_wwtpend_wwtpstart(hend, hstart):
    """function to calculate the elevation differences between the selected wwtp of each segment"""

    elev_diff_wwtpend_wwtpstart = hend - hstart
    return elev_diff_wwtpend_wwtpstart

calc_elev_diff_wwtpend_wwtpstart(elevation[1],elevation[0])