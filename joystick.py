from evdev import InputDevice, categorize, ecodes

def rotateGross(value, center_pos):
	if value < (center_pos - 50):
        	print("Coarse Rotate Left")
	elif value >= (center_pos - 50) and value <= (center_pos + 50):
		print("No Coarse Rotation")
        else:
		print("Coarse Rotate Right")
#	print("Z_AXIS EVENT - VAL: {}".format(keyevent.event.value))		

def rotateFine(value, center_pos):
	if value < (center_pos - 25):
		print("Fine Rotate Left")
	elif value >= (center_pos - 25) and value <= (center_pos + 25):
		print("No Fine Rotation")
	else:
		print("Fine Rotate Right")
#	print("Y_AXIS EVENT - VAL: {}".format(keyevent.event.value))

def tilt(value, center_pos):
	if value < (center_pos - 50):
        	print("Tilt Downward")
	elif value <= (center_pos - 50) and value >= (center_pos + 50):
		print("No Rotation")
        else:
		print("Tilt Upward")
#	print("X_AXIS EVENT - VAL: {}".format(keyevent.event.value))

gamepad = InputDevice('/dev/input/event0')
for event in gamepad.read_loop():
	if event.type == ecodes.EV_ABS:
		event = categorize(event).event
		if event.code == 5:
			rotateFine(event.value, 256)
		elif event.code == 1:
			tilt(event.value, 512)
		elif event.code == 0:
			rotateGross(event.value, 512)
