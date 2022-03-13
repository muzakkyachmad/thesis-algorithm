
#raw algorithm for thesis 14 feb - 10 mar 2022 based on the excel calculations and using dijkstra algorithm

(
    {"wwtp": "A", "X": 715551, "Y": 3515856},
    {"wwtp": "B", "X": 715379, "Y": 3512958},
)

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
