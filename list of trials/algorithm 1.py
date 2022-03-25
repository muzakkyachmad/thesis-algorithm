
#data of WWTP a=0 and b=1 and simulating route ba

wwtp_list = [0, 1]
h_wwtp_a = 495
h_wwtp_b = 534
h_wwtp_c = 382
hmax_segment_ab = 639
hmax_segment_ac = 646
hmax_segment_bc = 639
distance_a_to_hmax_of_segment_ab = 3051.71
distance_a_to_hmax_of_segment_ac = 1071.94
manning_coeff = 0.013
ks = 0.0015
viscosity = 0.000001
gravity_coeff = 9.81
efficincy_pump = 0.8
water_density = 1000

#functions to calculate the elevation difference between selected wwtp
def elev_diff_wwtp():
    data_ab = {
        "h_wwtp_a" : 495,
        "h_wwtp_b" : 534
    }

    elev_diff_wwtp = data_ab["h_wwtp_b"] - data_ab["h_wwtp_a"]
    print(elev_diff_wwtp)

elev_diff_wwtp():
if (elev_diff_wwtp > 0):
    return elev_diff_hmax
else:
    return diameter_pipe1_no_pump



#function to calculate elevation difference between hmax and wwtpa
def elev_diff_hmax():
    elevation_data = {
        "hmax_segment_ab": 639,
        "h_wwtp_a": 495,
        "h_wwtp_b": 534,
    }
    elev_diff_hmax = elevation_data["hmax_segment_ab"] - elevation_data["h_wwtp_a"]
    print(elev_diff_hmax)

elev_diff_hmax()

#function to calculate distance of pipe without pumping
def diameter_pipe1_no_pump():
    data3 = {"flowrate_ab": 0.0134,
        "slope_to_hmax": 0.002,
        "manning_coef": 0.013,
    }
    diameter_pipe1_no_pump = (((data3["flowrate_ab"] * data3 ["manning_coef"]) / (0.3117 * (data3["slope_to_hmax"] ** 0.5))) ** 0.375)
    print(diameter_pipe1_no_pump)

diameter_pipe1_no_pump()





