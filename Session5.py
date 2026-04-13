# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 22:26:58 2026

@author: marpl
"""

import numpy as np 
from astropy.table import Table

x = np.linspace(0, 2*np.pi, 1000)
sin_x = np.sin(x)


def main():
    ta = Table([[x],[sin_x]],None,["x", "sin(x)"],[float, float])
    print(ta)


if __name__ == "__main__":
    main()