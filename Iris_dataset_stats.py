#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

data = pd.read_csv("C:\\Users\\2204a\\Downloads\\iris_csv.csv")

print(data)

#Counting no. of times a particular species has appeared in the classes column
print(data["class"].value_counts())

iris_setosa = data[0:50]
iris_versicolor = data[50:100]
iris_virginica = data[100:150]

#IRIS SETOSA
sepal_length_1 = data.loc[0 : 50,["sepallength"]].sum()
sepal_width_1 = data.loc[0 : 50,["sepalwidth"]].sum()
petal_length_1 = data.loc[0 : 50,["petallength"]].sum()
petal_width_1 = data.loc[0 : 50,["petalwidth"]].sum()

print("\nAverage Iris Setosa: ", str(sepal_length_1/50), str(sepal_width_1/50), str(petal_length_1/50), str(petal_width_1/50))

#IRIS VERSICOLOR
sepal_length_2 = data.loc[0 : 50,["sepallength"]].sum()
sepal_width_2 = data.loc[0 : 50,["sepalwidth"]].sum()
petal_length_2 = data.loc[0 : 50,["petallength"]].sum()
petal_width_2 = data.loc[0 : 50,["petalwidth"]].sum()

print("\nAverage Iris Versicolor: ", str(sepal_length_2/50), str(sepal_width_2/50), str(petal_length_2/50), str(petal_width_2/50))

#IRIS VIRGINICA
sepal_length_3 = data.loc[0 : 50,["sepallength"]].sum()
sepal_width_3 = data.loc[0 : 50,["sepalwidth"]].sum()
petal_length_3 = data.loc[0 : 50,["petallength"]].sum()
petal_width_3 = data.loc[0 : 50,["petalwidth"]].sum()

print("\nAverage Iris Virginica: ", str(sepal_length_3/50), str(sepal_width_3/50), str(petal_length_3/50), str(petal_width_3/50))


#Following function must be apopended with the above data to simplify the code
def variance(data):
    n = len(data)
    list = []
    mean = mean()
    sum = 0
    
    for i in range(len(data)):
        data[i] = (data[i] - mean)**2
        list.append(data[i])
        
    for i in list:
        sum += i
        variance = sum / (n-1)
        return variance
    
def std_dev(variance):
    std_dev = variance**(1/2)
    return std_var

