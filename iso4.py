import pandas as pd
from pyiso4.ltwa import Abbreviate

abbreviator = Abbreviate.create()
df  = pd.read_csv("Q1.csv")
row_list = df.values.tolist()
ctr = 0
for i in row_list:

    str = i[0]
    print(abbreviator(str, remove_part=True))
