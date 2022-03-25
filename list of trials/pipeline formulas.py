


wwtp_data = [
    {"name": "A", "X": 715551, "Y": 3515856, "elevation": 495, "flow rate": 0.0134, "population": 21495},
    {"name": "B", "X": 715379, "Y": 3512958, "elevation": 534, "flow rate": 0.0130, "population": 26393},
    {"name": "C", "X": 716727, "Y": 3518696, "elevation": 382, "flow rate": 0.0001, "population": 94},
]

hmax_segment_elevation = {
    (0, 1): 639,
    (1, 0): 639,
    (0, 2): 646,
    (2, 0): 646,
    (1, 2): 639,
    (2, 1): 639,
}

hmax_segment_length_to_hmax = {
    (0, 1): 3051.71,
    (1, 0): 2014.57,
    (0, 2): 1071.94,
    (2, 0): 4490.03,
    (1, 2): 1865.13,
    (1, 2): 6968.66,
}

#compilation of data that should be inputted on the algorithm


#WWTP data

wwtp_7_coordinates = (
    {"wwtp": "A", "X": 715551, "Y": 3515856},
    {"wwtp": "B", "X": 715379, "Y": 3512958},
)

graph_7_wwtp_calculate = {
        'A':{'B':2903,'C':3073,'F':1866,'G':2198},
        'B':{'A':2903,'C':5894,'F':2171,'G':5079},
        'C':{'A':3073,'B':5894,'F':4162,'G':1604},
        'D':{'E':2247,'F':3196},
        'E':{'D':2247,'F':3815},
        'F':{'A':1866,'B':2171,'C':4162,'D':3196,'E':3815,'G':3851},
        'G':{'A':2198,'B':5079,'C':1604,'G':3851}}

graph_7_wwtp_qgis = {
        'A':{'B':4776,'C':5597,'F':2491,'G':4480},
        'B':{'A':4776,'C':8506,'F':4551,'G':6945},
        'C':{'A':5597,'B':8506,'F':5854,'G':6397},
        'D':{'E':2909,'F':5201},
        'E':{'D':2909,'F':6324},
        'F':{'A':2491,'B':4551,'C':5854,'D':5201,'E':6324,'G':6974},
        'G':{'A':4480,'B':6945,'C':6397,'F':6974}



#1 calculate the straight distance between two wwtps
import math

wwtp_x1 = 715551
wwtp_y1 = 3515856
wwtp_x2 = 715379
wwtp_y2 = 3512958

#note : the formula is correct and valid for the distance in straight distance (not following the roads)
#to know the distance based on the road routes, should use qgis manually as a data between each WWTPs


distance_of_wwtp = math.sqrt(((wwtp_x1 - wwtp_x2) ** 2) + ((wwtp_y1 - wwtp_y2) ** 2))
print(distance_of_wwtp)



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




#checking and calculating the slope from starting point to the highest point of the segment

h_start = 495
h_end = 534
hmax_segment = 639

def calculate_elevation_difference_between_wwtp():
    elev_diff = h_end - h_start
    if (elev_diff > 0):
        return
    else:
        return calculate_the_distance_without_pumping

def calculate_the_pump_route():
    hmax_segment_1 = hmax_segment - h_start
    if (hmax_segment_1 > 0):
        return pumping
    else:
        return calculate_the_distance_without_pumping

def calculate_pumping_distance():
    segment_wwtp_start_to_hmax =  3051