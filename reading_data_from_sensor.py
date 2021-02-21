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
for channel in range(3):
    offsets[channel+1] = AnalogIn(ads,channel).value
    

while True:
    
    for channel in range(3):
        channels[channel+1] = AnalogIn(ads,channel).value - offsets[channel+1]

   # channel0=AnalogIn(ads,0)
    #channel1=AnalogIn(ads,1)
    #channel2=AnalogIn(ads,2)
    #channel3=AnalogIn(ads,3)
    print(f'{channels[1]} | {channels[2]} | {channels[3]} |')
    #print("{:>5}\t{:>5}".format(channel0.value,channel0.voltage))
    #print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(channel0.value,channel1.value,channel2.value,channel3.value,))
    # Pause for half a second.
    time.sleep(1)





