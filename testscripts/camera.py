import sys
sys.path.append('/usr/local/lib/python3.4/site-packages')

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
	ret, frame = cap.read()

	if ret:
        	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		

        	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
