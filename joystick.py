from evdev import InputDevice, categorize, ecodes
gamepad = InputDevice('/dev/input/event0')
for event in gamepad.read_loop():
	if event.type == ecodes.EV_ABS:
		keyevent = categorize(event)
#		print("KEYEVENT: {}".format(keyevent))
#		print("EVENT: {}".format(keyevent.event))
#		print("CODE: {}".format(keyevent.event.code))
#		print("VALUE: {}".format(keyevent.event.value))
		if keyevent.event.code == 5:
			print("Z_AXIS EVENT - VAL: {}".format(keyevent.event.value))		
		elif keyevent.event.code == 1:
			print("X_AXIS EVENT - VAL: {}".format(keyevent.event.value))
		elif keyevent.event.code == 0:
			print("Y_AXIS EVENT - VAL: {}".format(keyevent.event.value))
