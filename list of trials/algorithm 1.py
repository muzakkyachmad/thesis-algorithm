
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
def elev_diff_wwtp(etp1, etp2):
    data_ab = {
        "h_wwtp_a" : 495,
        "h_wwtp_b" : 534
    }
if elev_diff_wwtp(495, 534) > 0:
    #to do if it is positive
else:
    #to do if it is negative

    elev_diff_wwtp = data_ab["h_wwtp_b"] - data_ab["h_wwtp_a"]
    print(f"the difference is {elev_diff_wwtp} meter")

elev_diff_wwtp()

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
