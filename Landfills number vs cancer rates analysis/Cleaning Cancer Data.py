#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Setup 

import pandas as pd
import numpy as np


# In[2]:


# Storing Path

cancer_data = "Resources/County_Cancer_Data.csv"


# In[5]:


# Reading in the data

county_cancer_df = pd.read_csv(cancer_data)
county_cancer_df.head()


# In[ ]:


# Split out county and stae into separate columns

county_cancer_df = 


# In[9]:


# Remove unnecessary columns from the dataframe

reduced_county_cancer_df = county_cancer_df[["State","Age-Adjusted Incidence Rate(†) - cases per 100,000","Average Annual Count","Recent Trend", ]]
reduced_county_cancer_df.head()


# In[ ]:


#

