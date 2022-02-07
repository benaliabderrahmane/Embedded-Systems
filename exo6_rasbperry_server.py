#!/usr/bin/python
from sense_hat import SenseHat
import time
import socket

sense = SenseHat()
sense.set_imu_config(True, False, False) #Magnemoter only

s = socket.socket()
host = '192.168.137.166' #ip of raspberry pi
port = 12345
s.bind((host, port))
s.listen(5)

c, addr = s.accept()
north = sense.get_compass()
print ('Got connection from',addr)
c.send('North : {}'.format(north))
c.close()
