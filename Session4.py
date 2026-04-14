# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:46:45 2026

@author: marpl
"""

class Animal:
     
     def __init__(self, name="", armLength=5.0, legLength=5.0, eyes=2,tail=False, furry=False):
         self.name = name
         self.armLength = armLength
         self.legLength = legLength
         self.eyes = eyes
         self.tail = tail
         self.furry = furry

     def aniprint(self):
         if self.furry == True :
             furPhrase = "furry"
         else:
            furPhrase = "non-furry"
         if self.tail == True:
            tPhase = "with a tail"
         else:
            tPhase = "with no tail"
            
         print(f"A {furPhrase} {self.name} {tPhase} has {self.eyes} eyes and an arm length of {self.armLength}, while also having a leg length of {self.legLength}")
         
    
rabbit = Animal("Rabbit", 1.0, 1.5, 2, True, True)
rabbit.aniprint()


    