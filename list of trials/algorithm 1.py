
#decision making algorithm of pumping and using assumption wwtp --> a = 0, b = 1, c = 2. below is the inputted data

wwtp_data = [
    {"name": "A", "X": 715551, "Y": 3515856, "elevation": 495, "flow rate (m3/s)": 0.0134, "population (lives)": 21495},
    {"name": "B", "X": 715379, "Y": 3512958, "elevation": 534, "flow rate (m3/s)": 0.0130, "population (lives)": 26393},
    {"name": "C", "X": 716727, "Y": 3518696, "elevation": 382, "flow rate (m3/s)": 0.0001, "population (lives)": 94},
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

#checking and calculating the slope from starting point to the highest point of the segment

def calculate_elevation_difference_between_wwtp(wwtp_data):
    elevdiff = wwtp_data[elevation[0]] - wwtp_data[elevation[2]]

calculate_elevation_difference_between_wwtp()






