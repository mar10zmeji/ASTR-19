#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0,2*np.pi, 100)

def newFunc(a=0.0,b=0.0):
    return a*np.exp(-b*x)


# In[4]:


y = newFunc(a=4.0,b=3.0)
def imgPlot(x,y, fname='session1plot.png'):
    f,ax = plt.subplots(1,1,figsize=(4,4))
    ax.plot(x,y,color="blue",linewidth=1.5)

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    plt.savefig(fname, format="pdf")
imgPlot(x,y)


# In[ ]:




