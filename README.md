 # Force-sensor Design 


The following step for the design of the sensor has been completed.
      
 ## 1. Mechanical design of sensor prototype has been done in solid work with following component and printed
  <img src="https://github.com/razainno/force-sensor/blob/main/mechanical_part.JPG" width="550" height="400">
  
  
  
   ## 2. electrical protype using four opto sensor is the following
 3. <img src="https://github.com/razainno/force-sensor/blob/main/photo5879850171876095368.jpg" width="300" height="300">



 ## 3. Raw data reading
 When obstacle inturrupt the path of from four sensors and voltage decreased, these vlaue with help of Adc has been converted into digital value and feed into raspberry pi for process where we can read the Raw data

 ## 4. Save the data for different weight (0kg ,0.5kg, 1.25kg, 1.75kg
Different value of the weight has been put n the sensor and value for the voltage has been save for all four sensors
 ## 5. Calculation of the weights for using least square method 
 AS we now that at statring point the there is no value for the sensor voltage because no for force has been applied 
 form equation F=V1xw1+V2xw2+V3xw3+V4xw4, the weight(w1,w2,w3,w4) has been calculated using least square method 
 ##  6. Calculation of the force using above calculated weights
 after callculation of the weight of the force can been calculated with  eqaution F=V1xw1+V2xw2+V3xw3+V4xw4 
  ## 7. Test the sensor for applying different force
 Applying random force and following result for calibrated sensor has been produced.
 
  <img src="https://github.com/razainno/force-sensor/blob/main/calibration_1.JPG" width="1200" height="500">
  ## 8. PCB Board design
  The whole design is created in Altium designer output can be seen below in images
  <p float="left">
  <img src="https://github.com/razainno/force-sensor/blob/main/Electrical_Design/top.JPG" width="100" />
  <img src="https://github.com/razainno/force-sensor/blob/main/Electrical_Design/bottom.JPG" width="100" /> 
</p>
 



           
