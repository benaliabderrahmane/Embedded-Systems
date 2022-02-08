# Embedded-Systems

Embedded Systems Project -HAE912E-

- BENALI Abderrahmane 
- BELLILA Ahmed Nassim 
- BOUZIT Zakaria

# exercice 1

Reference [GitHub Pages](https://pages.github.com/).

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

# exercise 2

The Sense HAT has an 8 × 8 RGB LED matrix, a five – button joystick and includes the following sensors:  

Gyroscope  
Accelerometer  
Magnetometer  
Temperature  
Barometric pressure  
Humidity  

Gyroscope – Wikipedia  

A gyroscope is a spinning wheel or disc in which the axis of rotation is free to assume any orientation by itself. (It’s an instrument or device that detects the angle (attitude), angular velocity or angular acceleration of an object.)  

Accelerometer – Wikipedia  

An accelerometer is a device that measures proper acceleration. (A compact accelerometer (acceleration sensor) is fabricated using MEMS technology. MEMS accelerometers are used for automotive airbags, car navigation inclinometers, game controllers, etc.)  

Acceleration – Wikipedia  

Acceleration, in physics, is the rate of change of velocity of an object with respect to time. An object’s acceleration is the net result of any and all forces acting on the object, as described by Newton’s Second Law. Accelerations are vector quantities (they have magnitude and direction).  

Magnetic sensor – Wikipedia  

A magnetometer is an instrument that measures magnetism—either magnetization of magnetic material like a ferromagnet, or the direction, strength, or the relative change of a magnetic field at a particular location.    

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
the goal is to use the gyroscope to control the moves of a LED on the screen, for that first we calibrate the gyroscope sensor (senseHat calibration already discussed above) then we suppose having the led on the middle (x=4 y=4) on and each time we move the raspberry we move the led in x and y directions, the led movement is supposed to be opposite to the one of the gyroscope (imitating the movement used in mobile games that uses gyroscope) also when we reach the limits we re-initialize to 0 or 7 depending on the limit.
# exercise 6
For both server and client we used Socket library available on python.

Soket provides a way of connecting two nodes on a network to communicate with each other. One socket (Server ie : Raspberry, ex : '192.168.137.166') listens on a particular port at an IP (Raspberry IP), while the other socket (Client) reaches out to the other to form a connection. The server forms the listener socket while the client reaches out to the server.

Next, all we need it to get the north direction from SenseHat (north = sense.get_compass()) then send it from the server (Raspeberry) to the local computer client. 
