import pandas as pd
import numpy as np

def separate(n):
    temp1 = str(n.index)
    temp2 = temp1.split("'")[1]
    result = temp2.split(":")[0]
    return result
    

dataframe = pd.read_csv('C:/Users/anast/AppData/Local/Temp/HW1-data.csv', 
                        delimiter = ",")
rate = np.mean(dataframe)
actual_series = rate[2:]
max_rate = max(actual_series)
temp = actual_series[actual_series == max_rate]
finish_result = separate(temp)

print(finish_result)

