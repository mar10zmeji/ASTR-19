#!/usr/bin/env python
# coding: utf-8

# In[115]:


import matplotlib.pyplot as plt
import numpy as np 
from scipy.optimize import curve_fit

pointN = 100
x = np.linspace(0,2*np.pi, pointN)


def model1(x, a,b):
    y0 = a*np.exp(-b*x)
    return y0

scale = np.linspace(2, 0.2, 100)
y = model1(x, 4.0,3.0)
scatter_y = y + np.random.normal(scale=scale, size=pointN) 
params0, parcov0 = curve_fit(model1, x, scatter_y, sigma=scale)


def model2(x, a,b):
    y1 = a/(x**b)
    return y1
params1, parcov1 = curve_fit(model2, x, scatter_y, sigma=scale)
# I don't know how to fix the covariance not working for this model

def FigPlot(x,y):

    yfit0 = model1(x,params0[0], params0[1])
    yfit1 = model2(x,params1[0], params1[1])

    f,ax = plt.subplots(1,1,figsize=(4,4))

    plt.errorbar(x,scatter_y, scale, fmt="o", color="salmon", label="scattered data",zorder=1)
    plt.plot(x,yfit0,zorder=3,color="green",label="Model 1")
    plt.plot(x,yfit1,zorder=2,color="blue",label="Model 2")

    ax.set_xlabel("x")
    ax.set_ylabel("y (with scatter)")
    ax.legend()
    print(f"The best fit for a and b in Model 1 are {params0[0]} and {params0[1]}, while Model 2 has them at {params1[0]} and {params1[1]}")
    plt.savefig("session3plot.pdf", format="pdf")
FigPlot(x,y)




# In[ ]:




