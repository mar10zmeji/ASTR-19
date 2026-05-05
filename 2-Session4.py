#!/usr/bin/env python
# coding: utf-8

# In[27]:


import numpy as np
import matplotlib.pyplot as plt

coolRandom = np.random.standard_cauchy(1000)


# In[28]:


gr = plt.hist(coolRandom, 100)
plt.savefig("Session4plot.pdf", format="pdf")


# In[ ]:




