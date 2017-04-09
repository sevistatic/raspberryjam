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
