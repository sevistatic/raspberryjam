raspberry jam
---
Author: Spencer Bryant

This project is the software implementation of a joystick-controlled RF Jammer for the Raspberry Pi 3. It was made for the CS 4999 Senior Design capstone course at Wright State University.
The application allows the user to operate a joystick which in turn moves an armature using stepper motors. The armature in question for the course was outfitted with a Logitech USB Camera and a Narrow-Field Yagi Antenna.

RF Jamming is illegal in the united states, so this project will not disclose any information on that part of the project, nor will I offer any help making, buying, or importing a jammer into the United States.


Dependencies:
 - Python 3.4 or later
 - PyQt5
 - opencv3 from the python cv2 package
 - python-evdev
 - RPi
 - virtualenv

Instructions:
source virtualenv configuration
`source /usr/local/bin/virtualenvwrapper.sh`

source your profile
`source ~/.profile`

connect to the setup virtualenv, <py3> is here in place of the one created during the virtualenv process
`workon py3`

navigate to the install directory

run the program
'python main.py'


Known bugs:
 - sometimes the camera feed does not initialize when the program starts. Restarting the program usually fixes this.
 - warnings about cleaning up GPIO pins that have not yet been set up sometimes show when the program ends
 - warnings about setting up GPIO pins which have not yet been deallocated sometimes show when the program starts. This is related to the above issue
 - libjpeg warnings about JPEG corruption show on every frame update. this is a bug in the libjpeg libraries with respect to video captures
 - the warning `libEGL warning: DRI2: failed to authenticate` shows when the program starts. It does not affect performance.
