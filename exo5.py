from sense_hat import SenseHat
import time 


sense = SenseHat()

#turn off all the leds
sense.clear()
x=4
y=4
sense.set_imu_config(False, True, False)
orientation_old = sense.get_orientation_degrees()
r_old = round(orientation_old["roll"],0) #for y 
p_old = round(orientation_old["pitch"],0)#for x

sense.set_pixel(x,y,(255,0,0))

while True:
	#turn off all the leds
	sense.set_imu_config(False, True, False)
	orientation = sense.get_orientation_degrees()
	r=round(orientation["roll"],0)#for y 
	p=round(orientation["pitch"],0)#for x
	if (r-r_old)>10:
		y=y+1
		r_old=r
		sense.clear()
	if (r_old-r)>10:
		y=y-1
		r_old = r
		sense.clear()
	if (p-p_old)>10:
		x=x-1
		p_old=p
		sense.clear()
	if (p_old-p)>10:
		x=x+1
		p_old=p
		sense.clear()
	if x>7:
		x=0
	if y>7:
		y=0
	if x<0:
		x=0
	if y<0:
		y=0
	sense.set_pixel(x,y,(255,0,0))

