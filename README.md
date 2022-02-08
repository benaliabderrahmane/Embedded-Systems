# Embedded-Systems

Embedded Systems Project -HAE912E-

- BENALI Abderrahmane 
- BELLILA Ahmed Nassim 
- BOUZIT Zakaria

# exercice 1 - Configuration
First of all, we need to configure the Raspberry, for that we use a screen and a keyboard. And we follow the instructions : 
1.We set the raspberry informations using raspi-config, it's a configuration tool in Raspbian which enables you to configure various settings of your Raspbian installation, such as the keyboard layout, the timezone, the password for the pi user, the SSH access, etc.
```
sudo raspi-config
```
We set the localizalition and the auto-connect network connection.

2.We add the Network Details to your Raspberry Pi. We open the wpa-supplicant configuration file in nano:
```
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```
and we add the following 
```
network={
    ssid="12345678"
    psk="87654321"
}
```
and we set the Raspebbry password : 
```
raspberry 1 : user : pipi - password : 123
raspberry 2 : user : raspberry pi - password : 123
```
Reference [Configuration](https://www.raspberrypi.com/documentation/computers/configuration.html).

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
Reference [Calibration](https://raspberrytips.com/sense-hat-tutorial-2/).

# exercise 2

The Sense HAT has an 8 × 8 RGB LED matrix, a five – button joystick and includes the following sensors:  
```
Gyroscope  
Accelerometer  
Magnetometer  
Temperature  
Barometric pressure  
Humidity  
```
- Gyroscope – Wikipedia  

A gyroscope is a spinning wheel or disc in which the axis of rotation is free to assume any orientation by itself. (It’s an instrument or device that detects the angle (attitude), angular velocity or angular acceleration of an object.)  

- Accelerometer – Wikipedia  

An accelerometer is a device that measures proper acceleration. (A compact accelerometer (acceleration sensor) is fabricated using MEMS technology. MEMS accelerometers are used for automotive airbags, car navigation inclinometers, game controllers, etc.)  

- Acceleration – Wikipedia  

Acceleration, in physics, is the rate of change of velocity of an object with respect to time. An object’s acceleration is the net result of any and all forces acting on the object, as described by Newton’s Second Law. Accelerations are vector quantities (they have magnitude and direction).  

- Magnetic sensor – Wikipedia  

A magnetometer is an instrument that measures magnetism—either magnetization of magnetic material like a ferromagnet, or the direction, strength, or the relative change of a magnetic field at a particular location.    

# exercise 3
sudo i2cdetect -y 1    

```  
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f  
00:          -- -- -- -- -- -- -- -- -- -- -- -- --  
10: -- -- -- -- -- -- -- -- -- -- -- -- 1c -- -- --  
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
40: -- -- -- -- -- -- UU -- -- -- -- -- -- -- -- --  
50: -- -- -- -- -- -- -- -- -- -- -- -- 5c -- -- 5f  
60: -- -- -- -- -- -- -- -- -- -- 6a -- -- -- -- --  
70: -- -- -- -- -- -- -- --  
```

Thus, i2c adresses used are :   
```
0x46, used by : led2472g, the led screen.  
0x1c & 0x6a, used by : LSM9DS1 Inertial Module (IMU), system-in-package featuring a 3D digital linear acceleration sensor, a 3D digital angular rate sensor, and a 3D digital magnetic sensor.  
0x5c, used by : lps25h, Pressure sensor.  
0x5f, used by : hts221, Humidity sensor.  
```
# exercise 4
the goal here is to measure the humidity and the temperature for that we use the senseHat functions
```
sense.get_temperature()
get_humidity()
```
then we display the values on the terminal.

# exercise 5
the goal is to use the gyroscope to control the moves of a LED on the screen, for that first we calibrate the gyroscope sensor (senseHat calibration already discussed above) then we suppose having the led on the middle (x=4 y=4) on and each time we move the raspberry we move the led in x and y directions, the led movement is supposed to be opposite to the one of the gyroscope (imitating the movement used in mobile games that uses gyroscope) also when we reach the limits we re-initialize to 0 or 7 depending on the limit.
# exercise 6
For both server (exo6_rasbperry_server.py) and client (exo6_computer_client.py) we used Socket library available on python.
```
socket.socket()
```
Soket provides a way of connecting two nodes on a network to communicate with each other.

One socket (Server ie : Raspberry, ex : '192.168.137.166') listens on a particular port at an IP (Raspberry IP), while the other socket (Client) reaches out to the other to form a connection. The server forms the listener socket while the client reaches out to the server.

Next, all we need it to get the north direction from SenseHat 
```
north = sense.get_compass()
```
then send it from the server (Raspeberry) to the local computer client. 

Reference [Socket](https://www.geeksforgeeks.org/socket-programming-python/).

# exercise 7 - SenseHat c++
here we need to set the SenseHat library available for c++, we need to : 

1.Clone the Repository
```
pi@raspberry:~ $ git clone https://github.com/PhilippeSimier/SenseHat.git
pi@raspberry:~ $ cd SenseHat/
```
2.install
```
pi@raspberry:~/SenseHat $ make
pi@raspberry:~/SenseHat $ sudo make install
pi@raspberry:~/SenseHat $ make clean
```
Now, we can demonstrate with the example exo7.cpp (Temperature and acceleration measurement) :
```
#include <SenseHat.h>
sense.Effacer()
sense << setcouleur()
sense << setrotation()
sense.ObtenirTemperature()
sense.ObtenirAcceleration()
```
Reference [SenseHat c++](https://github.com/PhilippeSimier/SenseHat).
