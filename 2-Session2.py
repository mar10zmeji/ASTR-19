#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0,2*np.pi, 100)


def newFunc(a=0.0,b=0.0):
    return a*np.exp(-b*x)


# In[50]:


y = newFunc(a=4.0,b=3.0)
scale = np.linspace(2, 0.2, 100)
def imgPlot(x,y, fname='session2plot.png'):
    scatter_y = np.random.normal(y, scale) 
    f,ax = plt.subplots(1,1,figsize=(4,4))

    plt.errorbar(x,scatter_y, scale, 0, fmt="none", ecolor="red")
    ax.scatter(x,scatter_y,color="red")

    ax.set_xlabel("x")
    ax.set_ylabel("y (with scatter)")
    plt.savefig(fname, format="pdf")
imgPlot(x,y)


# In[ ]:




