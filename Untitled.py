#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd


# In[7]:


data = pd.read_csv("pokemon.csv")
data.isnull().sum()


# In[11]:


data.iloc[0:3,:-1]


# In[12]:


data.describe()


# In[17]:


data = pd.read_csv("pokemon.csv")
data.head(n=11)


# 

# # one hot-encoding

# In[13]:


data


# In[15]:


data.isnull().sum()


# In[23]:


data["Type 2"].mean()
data.replace(to_replace="NaN",value=84,implace=True)


# In[19]:


attack_mean = data["Attack"].mean()
def set_attackk(val):
    if val < attack_mean:
        return "Attack Low
    else:
        return "Attack High"


# In[ ]:





# In[22]:


attack_mean = data["Attack"].mean()
def set_attack(val):
    if val < attack_mean:
        return "Attack Low"
    else:
        return "Attack High"


# In[24]:


data["Attack_hign_low"]=data["Attack"].apply(set_attack)
data


# In[6]:


data = pd .read_csv("pokemon.csv")
data . head()


# In[8]:


data[Attack_hign_low]=data["Attack"].apply(set_attack)


# In[ ]:




