
#decision making algorithm of pumping

def wwtp_data(name, x, y, h, population, flowrate, cost):
    wwpt_list = {
        "wwtp": "A", "X": 715551, "Y": 3515856,
        "wwtp": "B", "X": 715379, "Y": 3512958,

    }



#input related data of wwtp --> a = 0, b = 1, c = 2

wwtp_coordinates = {
    0: (715551, 3515856),
    1: (715379, 3512958),
    2: (716727, 3518696)
}

wwtp_elevation = {
    0 : 495,
    1 : 534,
    2 : 382
}

hmax_segment = {
    (0, 1): 639,
    (1, 0): 639,
    (0, 2): 646,
    (2, 0): 646,
    (1, 2): 639,
    (1, 2): 639
}

wwtp_population = {
    0: 21495,
    1: 26393,
    2: 94
}

wwtp_flowrate = {
    0: 0.0134,
    1: 0.0130,
    2: 0.0001
}


#calculate the slope from starting point to the highest point of the segment

h1 = 495
h2 = 534

if (h2-h1) > 0:
    difference_elevation = h2 - h1
elif (h2-h1) <= 0:
    print("there is no pumping in this segment")


slope_to_hmax = (2.33 * 0.0001 * (0.134 ** (-0.46)))


#3 calculate the diameter pipe (d_pipe1)

n = 0.013 #manning coefficient - assumed
slope = slope_to_hmax

diameter_pipe1 = ((( n * 0.0134)/(0.3117 * (slope ** 0.5))) ** 0.375)



#4 calculate the velocity in the pipe (v)

velocity = ((0.134 * 4) / (3.14 * (diameter_pipe1 ** 2)))



#calculate the reynolds number (re)

viscosity = 10 ** -6

Re = ((velocity * diameter_pipe1) / viscosity)


#calculate the ks/d value (ks_d)

ks_d = 0.0015 / diameter_pipe1


#calculate the head friction (hf)

friction_loss = 0.05 #assumption
gravity_coef = 9.81 #in m/s^2

head_friction = (friction_loss * distance_of_wwtp) / (diameter_pipe1 * 2 * gravity_coef)



#calculate the total of the headloss
headloss = head_friction + slope_to_hmax

#calculate the power of the pump

water_density = 1000 #in kg/m^3
pump_efficiency = 0.8 #assumed 80% efficient

pump_power = (((water_density * gravity_coef * headloss * 0.134) / pump_efficiency) / 1000)

#calculate the pipe1 construction cost (ILS)

pipe1_cost = 460 * distance_of_wwtp #460 ILS
print(pipe1_cost)
