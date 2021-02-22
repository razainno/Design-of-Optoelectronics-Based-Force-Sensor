## force-sensor
#The following step for the design of the sensor has been completed.


       #  1. Mechanical design AND electrical design  of the sensor has been created 
       # Result for halfcheetah robot by changing gravity_function value 

            1. Mechanical design of sensor prototype has been done in solid work with following component and printed
            ![Alt text](https://github.com/razainno/force-sensor/blob/main/mechanical_part.JPG
"Mechanical design of the sensor")
            3. electrical protype using four opto sensor is the following

         2.  When obstacle inturrupt the path of from four sensors and voltage decreased, these vlaue with help of Adc has been converted into digital value and feed into raspberry pi for process where we can read the Raw data

         3. Save the data for different weight (0kg ,0.5kg, 1.25kg, 1.75kg
Different value of the weight has been put n the sensor and value for the voltage has been save for all four sensors
         5. Calculation of the weights for using least square method 
 AS we now that at statring point the there is no value for the sensor voltage because no for force has been applied 
 form equation F=V1xw1+V2xw2+V3xw3+V4xw4, the weight(w1,w2,w3,w4) has been calculated using least square method 
 
         7. Calculation of the force using above calculated weights
         after callculation of the weight of the force can been calculated with  eqaution F=V1xw1+V2xw2+V3xw3+V4xw4 
         Test the sensor for applying different force
         10.Applying random force and following result for calibrated sensor
          

