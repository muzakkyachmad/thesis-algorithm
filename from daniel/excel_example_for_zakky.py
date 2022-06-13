# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a an example of using python with excel
"""

#import packages
import pandas as pd

df=pd.read_excel('example_input_data.xlsx') #creates DataFrame by reading excel file

df["distance_between_x_and_y"] = df["x-coord"] - df["y-coord"] #calculated new column

df.to_excel("example_output_data.xlsx", sheet_name="Output") #outputs the manipulated data into new excel file

