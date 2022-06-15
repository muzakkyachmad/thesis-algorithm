
from inputdatawwtp7sd import elevation


#A0
def calc_elev_diff_wwtpend_wwtpstart(hend, hstart): #this line is defining the function description, the formula, and the command to call it. - it will remain same to the others
    """function to calculate the elevation differences between the selected wwtp of each segment"""

    elev_diff_wwtpend_wwtpstart = hend - hstart #the formula to calculate the elevation difference
    print(elev_diff_wwtpend_wwtpstart)
    return elev_diff_wwtpend_wwtpstart

calc_elev_diff_wwtpend_wwtpstart(elevation[1],elevation[0])


