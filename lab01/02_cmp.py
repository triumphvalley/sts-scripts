#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 17:12:16 2021

@author: timo
"""
import numpy as np
import matplotlib.pyplot as plt
A= np.array([1, 2, 3, 4, 5]) #Anzahl der Flugreisen 
h= np.array([9, 8, 5, 7, 1]) #Absolute Häufigkeit 
n= np.sum(h) #Grösse der Stichprobe
f= h/n #relative Häufigkeit
H= np.cumsum(h) #absolute Summenhäufigkeit 
F= np.cumsum(f) #relative Summenhäufigkeit, kumulative Verteilungsfunktion(CDF)

A_p=np.concatenate((np.array([0]),A,np.array([6])),axis=0) 
h_p=np.concatenate((np.array([0]),h,np.array([0])),axis=0) 
H_p=np.concatenate((np.array([0]),H,np.array([n])),axis=0) 
f_p=h_p/n
F_p=np.cumsum(f_p)

plt.subplot(1,2,2)
plt.step(A_p, H_p,where='post') 
plt.title('Absolute Summenhäufigkeit') 
plt.xlabel('Anzahl Flugreisen') 
plt.ylabel('Anzahl Haushalte') 
plt.xlim(0,6)
plt.ylim(0,30)
plt.tight_layout()