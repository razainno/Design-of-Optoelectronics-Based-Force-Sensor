# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 13:40:58 2021

@author: Muhammad Ilyas Raza
"""

import numpy as np
import csv
import time
import matplotlib.pyplot as plt
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
i2c=busio.I2C(board.SCL,board.SDA)
ads=ADS.ADS1115(i2c)
print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)

channels = {}
offsets = {}

Force1=[]
Force2=[]
Error=[]
timeout = time.time() + 2*10  # 5 minutes from now

for channel in range(4):
    offsets[channel+1] = AnalogIn(ads,channel).value

    

while True:
    #f=open('data1.75_nkg.csv','a',newline="")
    #file=csv.writer(f)
    if time.time() > timeout:
        break
    
    for channel in range(4):
        channels[channel+1] = AnalogIn(ads,channel).value - offsets[channel+1]
    time.sleep(0.005)
    #F= channels[2]*(-0.49245174)+channels[3]*(1.03675718)+channels[4]*(-0.52497244)
    #s = np.random.uniform(-1,2)
    print(f'{channels[1]} | {channels[2]} | {channels[3]} | {channels[4]}|')
    F1= channels[3]*(0.0)+channels[4]*( -0.039085)
    F2=channels[1]*(0.0145)
    Force1.append(F1)
    Force2.append(F2)
    error=F2-F1
    if error < 0:
        error=error*(-1)
    Error.append(error)
    print(F1 ,"N")
    print(F2, "N")
    


plt.plot(Force1, color='b', label="our_Force_sensor")
plt.plot(Force2, color='r', label="Futek_Force_Senssors")
plt.title("Force comparison")
plt.xlabel("Time [ms]")
plt.ylabel("Force [N]")
plt.legend(loc='best')

plt.grid(color = 'black', linestyle = '--', linewidth = 0.7)
plt.show()

#Error graph
plt.plot(Error, color='r', label="error")

plt.title(" Force error between Futek and propsed sensor")
plt.xlabel("Time [ms]")
plt.ylabel("Force error [N]")
plt.ylim(-1,10)
plt.legend(loc='best')

plt.grid(color = 'black', linestyle = '--', linewidth = 0.7)
plt.show()


