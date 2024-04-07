import pandas as pd
import numpy as np
import logging

df = pd.read_csv("A_conferences.csv")
data = df['author'].tolist()

delimiter = "::"

# Configure logging
logging.basicConfig(filename='float_conversions.log', level=logging.INFO)

# Split list with logging for floats
split_list = []
for value in data:
    try:
        split_value = str(value).split(delimiter)
        split_list.append(split_value)
    except AttributeError:
        logging.info(f"Converted float value to string: {value}")
        split_list.append([str(value)])  # Wrap float in a single-element list

our_faculty = pd.read_csv("faculty.csv")
fac = our_faculty['scholar_name'].to_list()
fac = [x for x in fac if not pd.isna(x)]

output = {}

for i in split_list:
    for j in i:
        if(j in fac):
            b = len(i)
            output.update({j: 1/b})
            
print (output)

college = our_faculty['College']


