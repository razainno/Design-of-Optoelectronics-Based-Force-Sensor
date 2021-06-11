


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

Force=[]
timeout = time.time() + 2*5   # 5 minutes from now

for channel in range(3):
    offsets[channel+1] = AnalogIn(ads,channel).value

    

while True:
    #f=open('data1.75_nkg.csv','a',newline="")
    #file=csv.writer(f)
    if time.time() > timeout:
        break
    
    for channel in range(3):
        channels[channel+1] = AnalogIn(ads,channel).value - offsets[channel+1]
    time.sleep(0.005)
    F= channels[1]*(-0.49245174)+channels[2]*(1.03675718)+channels[3]*(-0.52497244)
   
    print(f'{channels[1]} | {channels[2]} | {channels[3]} |')
    F= channels[1]*(-0.4612532)+channels[2]*(0.92776894)+channels[3]*(-0.46739709)
    
    Force.append(F)
    print(F)
    


plt.plot(Force, color='b', label="Force")
plt.title("Sensor Calibration")
plt.xlabel("Time [ms]")
plt.ylabel("Force [N]")
plt.legend(loc='best')
plt.show()









