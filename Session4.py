# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:46:45 2026

@author: marpl
"""

class Animal:
     name = ""
     armLength: 5.0
     legLength: 5.0
     eyes: 2
     tail: True
     furry: True

def createAnimal(n, aL, lL, eye, t, f):
    anim = Animal()
    anim.name = n
    anim.eyes = eye
    anim.legLength = lL
    anim.armLength = aL
    anim.tail = t
    anim.furry = f
    print(f"A {anim.name} has {anim.eyes} eyes and an arm length of {anim.armLength}, while also having a leg length of {anim.legLength}")
    
createAnimal("Rabbit", 1.0, 1.5, 2, True, True)


    