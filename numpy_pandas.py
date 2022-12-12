import numpy as np
import pandas as pd

list_1 = ['a', 'b', 'c', 'd']
labels = [1,2,3,4]
ser_1 = pd.Series(data=list_1, index=labels)
ser_1

arr_1 = np.array([1,2,3,4])
ser_2 = pd.Series(arr_1)

dict_1 = {'f_name': "Abhijeet", 'l_name': "Solanki", 'age': 18 }
ser_3 = pd.Series(dict_1)

ser_4 = pd.Series({0:5, 1:6, 2:7, 3:8})

#many operation on the defined ser can be performed
ser_2 + ser_4