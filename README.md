# Embedded-Systems

**Embedded Systems Project -HAE912E-**

- BENALI Abderrahmane
- BELLILA Ahmed Nassim
- BOUZIT Zakaria

# SenseHat Calibration 
1.Install the requirements : 
```
sudo apt install octave -y

cp /usr/share/librtimulib-utils/RTEllipsoidFit ./ -a
```
2.Run the calibration tool :
```
cd RTEllipsoidFit

RTIMULibCal
```
3.A configuration menu like this shows up:
```
m - calibrate magnetometer with min/max

e - calibrate magnetometer with ellipsoid (do min/max first)

a - calibrate accelerometers

x - exit
```
we choose an option, then we have to move the Raspberry Pi in all directions on 6 axes.
Then we save.

Ref : [Sense-Hat calibration](https://raspberrytips.com/sense-hat-tutorial-2/).

# exercise 3
sudo i2cdetect -y 1    


  
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f  
00:          -- -- -- -- -- -- -- -- -- -- -- -- --  
10: -- -- -- -- -- -- -- -- -- -- -- -- 1c -- -- --  
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
40: -- -- -- -- -- -- UU -- -- -- -- -- -- -- -- --  
50: -- -- -- -- -- -- -- -- -- -- -- -- 5c -- -- 5f  
60: -- -- -- -- -- -- -- -- -- -- 6a -- -- -- -- --  
70: -- -- -- -- -- -- -- --  

Thus, i2c adresses used are :   
0x46, used by : led2472g, the led screen.  
0x1c & 0x6a, used by : LSM9DS1 Inertial Module (IMU), system-in-package featuring a 3D digital linear acceleration sensor, a 3D digital angular rate sensor, and a 3D digital magnetic sensor.  
0x5c, used by : lps25h, Pressure sensor.  
0x5f, used by : hts221, Humidity sensor.  

# exercise 4
the goal here is to measure the humidity and the temperature for that we use the senseHat library on python, then we display the values on the terminal using the print function.

# exercise 5
...

# exercise 6
