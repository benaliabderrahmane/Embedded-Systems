from sense_hat import SenseHat
import time


sense = SenseHat()
sense.clear()

while True:
	temp = round(sense.get_temperature(),2)
	humidity = round(sense.get_humidity(),2)
	print(' the temperature in the room is: {}'.format(temp))
	print(' the humidity in the room is: {}'.format(humidity))
	print('------------------------------')
	time.sleep(1)
