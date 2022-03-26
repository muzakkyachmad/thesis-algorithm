
#data of the wwtp - structure wwtpn = [elevation, flowrate(m3/s), population, and base cost] based on sd wwtp data
wwtp_sd1 = [497, 0.005, 4066,  ]
wwtp_sd2 = [467, 0.006, 4156, ]
wwtp_sd3 = [460, 0.002, 1129, ]
wwtp_sd4 = [330, 0.002, 1716, ]
wwtp_sd5 = [377, 0.012, 7036, ]
wwtp_sd6 = [383, 0.057, 45861, ]
wwtp_sd7 = [382, 0.035, 23281, ]

#data of 7 sd wwtp = length of each segment
hmax_segment_sd = [497, 537, 600, 600, 600, 530, 530, 600, 524, 557, 390, 520, 530, 530, 572, 575]


#data of the wwtp based on the python result
wwtp_p1 = [495, 0.005, 4066,  ]
wwtp_p2 = [467, 0.006, 4156, ]
wwtp_p3 = [460, 0.002, 1129, ]
wwtp_p4 = [330, 0.002, 1716, ]
wwtp_p5 = [377, 0.012, 7036, ]
wwtp_p6 = [383, 0.057, 45861, ]
wwtp_p7 = [382, 0.035, 23281, ]






wwtp_list = [0, 1]
h_wwtp_a = 495
h_wwtp_b = 534
h_wwtp_c = 382
hmax_segment_ab = 639
hmax_segment_ac = 646
hmax_segment_bc = 639
distance_a_to_hmax_of_segment_ab = 3051.71
distance_a_to_hmax_of_segment_ac = 1071.94


#hydraulic inputs
manning_coeff = 0.013
ks = 0.0015
viscosity = 0.000001
gravity_coeff = 9.81
efficincy_pump = 0.8
water_density = 1000



#function to calculate elevation difference between hmax and wwtpa
def elev_diff_hmax():
    hmax_data = {
        "hmax_segment_ab": 639,
        "h_wwtp_a": 495
    }
    elev_diff_hmax = hmax_data["hmax_segment_ab"] - hmax_data["h_wwtp_a"]
    print(elev_diff_hmax)

elev_diff_hmax()


#2 calculate the slope between the points

h1 = 489
h2 = 524
hmax = 639

slope_to_hmax = (2.33 * 0.0001 * (0.134 ** (-0.46)))
print(slope_to_hmax)

#3 calculate the diameter pipe (d_pipe1)

n = 0.013 #manning coefficient - assumed
slope = slope_to_hmax

diameter_pipe1 = ((( n * 0.0134)/(0.3117 * (slope ** 0.5))) ** 0.375)
print(diameter_pipe1)


#4 calculate the velocity in the pipe (v)

velocity = ((0.134 * 4) / (3.14 * (diameter_pipe1 ** 2)))
print(velocity)


#5 calculate the reynolds number (re)

viscosity = 10 ** -6

Re = ((velocity * diameter_pipe1) / viscosity)
print(Re)

#6 calculate the ks/d value (ks_d)

ks_d = 0.0015 / diameter_pipe1
print(ks_d)

#7 calculate the head friction (hf)

friction_loss = 0.05
gravity_coef = 9.81

head_friction = (friction_loss * distance_of_wwtp) / (diameter_pipe1 * 2 * gravity_coef)
print(head_friction)


#8 calculate the total of the headloss

headloss = head_friction + slope_to_hmax
print(headloss)

#10 calculate the power of the pump

water_density = 1000
pump_efficiency = 0.8 #assumed 80% efficient

pump_power = (((water_density * gravity_coef * headloss * 0.134) / pump_efficiency) / 1000)
print(pump_power)

#11 calculate the pipe1 construction cost (ILS)

pipe1_cost = 460 * distance_of_wwtp
print(pipe1_cost)
