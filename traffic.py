from gpiozero import LED, Button
from time import sleep
from signal import pause 

button = Button(2)
red = LED(21)
yellow = LED(19)
green =  LED(26)

def pressedStatus():
	if( green.is_active==True):
		green.off()
		yellow.on()
		sleep(2)
		yellow.off()
		red.on()
		sleep(5)
		red.off()
		yellow.on()
		sleep(2)
		yellow.off()
		green.on()
	else:
		red.on()
		sleep(5)
		red.off()
		yellow.on()
		sleep(2)
		yellow.off()
		green.on()



button.when_pressed = pressedStatus
pause()
