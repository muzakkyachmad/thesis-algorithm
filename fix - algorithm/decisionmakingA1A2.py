

from inputdatawwtp7sd import elevation
from inputdatawwtp7sd import hmax_segment_sd

#A. PART OF PUMPING - GREEN BOXES

#A1
def calc_elev_diff_hstart_hmax(hstart, hmax):
    """function to calculate the elevation differences from the starting wwtp
    to the highest point of the segment"""

    elev_diff_hstart_hmax = hmax - hstart
    print(elev_diff_hstart_hmax)
    return elev_diff_hstart_hmax

calc_elev_diff_hstart_hmax(elevation[0],hmax_segment_sd[0])


#A2
def calc_elev_diff_hmax_hend(hmax, hend):
    """function to calculate the elevation differences from the highest point to
    the end wwtp of the segment"""

    elev_diff_hmax_hend = hmax - hend
    print(elev_diff_hmax_hend)
    return elev_diff_hmax_hend

calc_elev_diff_hmax_hend(hmax_segment_sd[0], elevation[1])