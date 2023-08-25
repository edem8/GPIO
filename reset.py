from subprocess import call
from gpiozero import Button, LED
from signal import pause
from time  import sleep

button = Button(2)
led = LED(21)

def resetRaspberry():
	led.on()
	print("Reseting your Raspberry PI ...")
	sleep(3)
	led.off()
	print("\n...Reset Successful ...")

button.when_pressed =  resetRaspberry
pause()
