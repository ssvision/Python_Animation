# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 09:39:00 2021

@author: SOMDEB SAHA
"""

"""
code for creating a simple animation for an aeroplane
the motions are described in 2-D as:
    x = 800*t
    y = 200
"""






#importing required libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.gridspec as gridspec
###########################################

# creating time array

t0 = 0      #initial time
t_end = 2   # final time
dt = 0.005  #time interval or delta_t
#  np.arange ( start, stop, time_interval)... does not include stop variable
t = np.arange(t0, t_end+dt, dt) 

###########################################

#creating 2-D x and y data

x = 800 * t
y = 200 * np.ones(len(t)) 


################# animation ############################################

frame_amount = len(t) # this has to be kept same as time series length

def update_plot(num):
    # This function will update the line object at every animation interval
    plane_trajectory.set_data(x[0:num], y[0:num])
    
    return plane_trajectory,


fig = plt.figure(figsize=(16,9), dpi=120, facecolor=(0.8,0.8,0.8))  #set up the figure proporties
gs = gridspec.GridSpec(2, 2) # divide the figure into a matrix of (2,2)


ax0 = fig.add_subplot(gs[0,:], facecolor=(0.9,0.9,0.9)) #assign the first plot an area same as first row 
plane_trajectory, = ax0.plot([], [], 'g', linewidth=2)  #create a line object plane_trajectory which will be updated at every animation interval
plt.xlim(x[0],x[-1])
plt.ylim(100,250)


plane_ani = animation.FuncAnimation(fig, update_plot, frames=frame_amount, interval=20, repeat=True, blit=True)

plt.show()








