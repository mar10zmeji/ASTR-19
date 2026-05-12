#!/usr/bin/env python
# coding: utf-8

# In[117]:


import matplotlib.pyplot as plt
import numpy as np 

pointN = 100
x = np.linspace(0,2*np.pi, pointN)

def model1(x, a,b):
    y0 = a*np.exp(-b*x)
    return y0

scale = np.linspace(2, 0.2, 100)
y = model1(x, 4.0,3.0)

def FigPlot(x,y):
    f,ax = plt.subplots(1,1,figsize=(4,4))

    ax.plot(x,y,color="salmon")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    plt.savefig("session1plot.pdf", format="pdf")
FigPlot(x,y)




# In[ ]:




