#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 16:56:28 2021

@author: timo
"""

import numpy as np
import matplotlib.pyplot as plt

A = np.arange(0,7,1) #Mögliche Ergebnisse 
h = np.array([83, 25, 28, 18, 12, 10, 2]) #Absolute Häufigkeiten
f = h / h.sum() #relative Häufigkeiten

plt.figure(1)
plt.subplot(2, 1, 1)
plt.bar(A,h,0.4)
plt.ylabel('Absolute Häufigkeit') 
plt.xlabel('Würfelergebnisse') 
plt.title('Absolute Häufigkeitsfunktion - Säulendiagramm')
plt.tight_layout()


plt.subplot(2, 1, 2)
plt.bar(A,f,0.4)
plt.ylabel('Relative Häufigkeit') 
plt.xlabel('Würfelergebnisse') 
plt.title('Absolute Häufigkeitsfunktion - Säulendiagramm')
plt.tight_layout()