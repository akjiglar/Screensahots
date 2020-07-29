# pip install pillow
# pip install keyboard

from PIL import ImageGrab
import keyboard


def screenShot():
	sc = ImageGrab.grab() 
	sc.save("C:/Users/avinash/Pictures/Screenshots/screenshot.jpg")

while True:
	if keyboard.is_pressed('p'):
		screenShot()
		break