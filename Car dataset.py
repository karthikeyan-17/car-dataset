#!/usr/bin/env python
# coding: utf-8

# # Cars Dataset
# 
# The data of different cars is given with their specifications.
# I'm going to analyze this dataset using the Pandas DataFrame

# In[63]:


import pandas as pd


# In[37]:


car=pd.read_csv(r"C:\Users\Sathiyamurthy\Downloads\2. Cars Data1.csv")


# In[38]:


car.head()


# In[39]:


car.shape


# # i) Data Cleaning
# 
# Find all null value in the datasets.If there  is null then fill with the mean of that colummn.

# In[49]:


car.isnull().sum()


# In[50]:


car['Cylinders'].fillna(car['Cylinders'].mean(),inplace=True)


# # ii) Value counts
# 
# check what are the different types of make are there in our dataset.And,what is the count of each Make in the data

# In[51]:


car["Make"].value_counts()


# # iii)Instruction(Filtering)
# 
# Show all the records where Origin is Asia or Europe.

# In[53]:


car[car['Origin'].isin(['Asia','Europe'])]


# # iv)Removing unwanted records
# 
# Remove all the records where Weight is above 4000

# In[54]:


car[car['Weight']>4000]


# In[57]:


car[~(car['Weight']>4000)]


# # v)Applying function on a column
# 
# Increase all the values of "MPG_City" column by 3.

# In[62]:


car

