# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 13:39:03 2021

@author: Muhammad Ilyas Raza
"""

import numpy as np
import csv
import time
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


timeout = time.time() + 8*6   # 5 minutes from now

for channel in range(4):
    offsets[channel+1] = AnalogIn(ads,channel).value

    

while True:
    f=open('calibration_futek16.csv','a',newline="")
    file=csv.writer(f)
    if time.time() > timeout:
        break
    
    for channel in range(4):
        channels[channel+1] = AnalogIn(ads,channel).value - offsets[channel+1]
    time.sleep(0.005)
   
    
    #F1= channels[2]*(-0.2852532)+channels[3]*(0.92776894)+channels[4]*(-0.28739709)
    F2=channels[1]*(0.0143)
    print(f'{F2}  | {channels[4]}|')
    file.writerow([F2,channels[4]])
    
f.close()  
