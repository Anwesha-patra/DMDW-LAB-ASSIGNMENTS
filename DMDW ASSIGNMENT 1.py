#!/usr/bin/env python
# coding: utf-8

# ## FIND MEAN --SAMPLE 1

# In[1]:


(4+8+6+5+3+2+8+9+2+5)/10


# ## MEAN SAMPLE-2

# In[2]:


import statistics
statistics.mean([4,8,6,5,3,2,8,9,2,5])


# ### MEDIAN SAMPLE 1

# In[3]:


def my_median(sample):
    n=len(sample)
    index=n//2
    if n%2:
        return sorted(sample)[index]
    return sum(sorted(sample)[index - 1 : index+1])/2
my_median([3,5,1,4,2])


# ### MEDIAN SAMPLE 2

# In[4]:


import statistics
statistics.median([3,5,1,4,2])


# ### MODE SAMPLE 1

# In[5]:


from collections import Counter

def my_mode(sample):
    c = Counter(sample)
    return [k for k, v in c.items() if v == c.most_common(1)[0][1]]


my_mode(["male", "male", "female", "male"])


# ### MODE SAMPLE 2 

# In[6]:


mport statistics

statistics.mode([4, 1, 2, 2, 3, 5])


# ### VARIANCE SAMPLE 1

# In[7]:


def variance(data):
     # Number of observations
     n = len(data)
     # Mean of the data
     mean = sum(data) / n
     # Square deviations
     deviations = [(x - mean) ** 2 for x in data]
     # Variance
     variance = sum(deviations) / n
     return variance

variance([4, 8, 6, 5, 3, 2, 8, 9, 2, 5])


# ### VARIANCE SAMPLE 2 

# In[8]:


import statistics

statistics.pvariance([4, 8, 6, 5, 3, 2, 8, 9, 2, 5])


# ### STANDARD DEVIATION SAMPLE 1

# In[9]:


import math

 # We relay on our previous implementation for the variance
def variance(data, ddof=0):
     n = len(data)
     mean = sum(data) / n
     return sum((x - mean) ** 2 for x in data) / (n - ddof)

def stdev(data):
     var = variance(data)
     std_dev = math.sqrt(var)
     return std_dev

stdev([4, 8, 6, 5, 3, 2, 8, 9, 2, 5])


# ### STANDARD DEVIATION SAMPLE 2

# In[10]:


import statistics

statistics.pstdev([4, 8, 6, 5, 3, 2, 8, 9, 2, 5])


# In[ ]:




