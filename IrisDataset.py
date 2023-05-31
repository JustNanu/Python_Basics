#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#Importing Iris dataset
iris = pd.read_csv("iris_csv.csv")


# In[3]:


iris.head()


# In[5]:


#Basic Statistical tools for descriptive analysis
mean = pd.DataFrame(iris[["sepallength","sepalwidth", "petallength", "petalwidth"]].mean())
median = pd.DataFrame(iris[["sepallength","sepalwidth", "petallength", "petalwidth"]].median())
mode = pd.DataFrame(iris[["sepallength","sepalwidth", "petallength", "petalwidth"]].mode())
std = pd.DataFrame(iris[["sepallength","sepalwidth", "petallength", "petalwidth"]].std())


# In[6]:


#Creating dataframe 
mean.rename(columns = {0: "Mean"}, inplace = True)
median.rename(columns = {0: "Median"}, inplace = True)
mode.transpose().rename(columns = {0 : "Mode"}, inplace = True)
std.rename(columns = {0: "Std"}, inplace = True)


# In[7]:


df = pd.concat([mean, median, mode.transpose().rename(columns = {0 : "Mode"}), std], axis = 1)


# In[8]:


df


# In[9]:


df.reset_index(inplace = True)


# In[10]:


df


# In[11]:


#Mean graph with std
Graph = df.plot(kind = "bar", x = "index", y = "Mean", yerr = "Std")


# In[14]:


#Slicing the dataframe df to get one class at a time
iris_setosa = iris.head(50).drop("class", axis = 1)


# In[16]:


#Establishing correlation between all the variables
corr = iris_setosa.corr()
corr


# In[17]:


#Correlation Visualization using Heatmaps
sns.heatmap(corr)


# In[18]:


#Heatmap edit
sns.heatmap(corr, cmap = "RdBu", vmin = -1, vmax = 1, annot = True )


# In[ ]:




