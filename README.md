## PiWars Turkey 2020: Distributed by Hisar Cs for use in the PiWars Turkey competition.  
  
This python library was made for the purposes of making coding easier for the robot kits distributed by Hisar Cs for the PiWars Turkey Competition.  


## Setup

To install Pi20English use the pip packaging service [pip](https://pip.pypa.io/en/stable/),  and run the code below.


```
$ sudo pip3 install Pi20
```

Alternatively github can be used for the installation.
```bash git clone https://github.com/HisarCS/Pi20.git
$ git clone https://github.com/HisarCS/Pi20.git
$ cd Pi20
$ sudo python setup.py install
```

## Usage

```python
import Pi20
```
## Documentation

Currently the library has 5 modules:
-  simplifiedPiCam(To optimize and make the usage of OpenCV easier.)
- Controller (To make taking input from the PS3 controller using pygame easier.)
- MotorControl (To make using the pololuDRV8835 motor controllers easier to use.)
- ServoControl (To make using the Servo Motors through the GPIO pins easier.)
- UltrasonicSensor (To make using the HC-SR04 ultrasonic distance sensor easier to use.)

For performance reasosn this library uses multithreading. So that other pieces of running code wont be affected. Modules that use multithreading simplifiedPiCam (for displaying and taking the output of the camera), Controller (to continuously take input from the controller.) ve ServoControl (To stop it from disabling the main thread through sleep).

simplifiedPiCam:
-
- Methods

```python
__updateValues__()
```
Updates the frame by the values recieved from the PiCam inside a while loop.  Calling it in the main thread **Is not reccomended** since it will most likely get stuck on that line.

```python
startReadingValues()
```
Starts a new thread with the ``` __updateValues__()``` method called.  By calling this from the start you can access the camera values from anywhere in the code.

```python
readValues()
```
Returns the values from the camera as a NumPy list. This numpy list is updated continupusly in the ``` __updateValues__()``` method.

```python
__updateFrame__()
```
Makes a new openCV window with given parameters and updates it continuously. when "q" is pressed the window is closed. Calling it in the main thread **Is not reccomended** since it will most likely get stuck on that line.
```python
showSquare()
```
To start a window without slowing the mainthread, calls the  ``` __updateFrame__()``` method in another thread. It takes two parameters, being the windows name and what will be displayed. By entering different paramaters and calling it in a while loop you can update the values. If no parameters are given the method will use the placeholder values of the title called 'frame' and the raw output of the PiCam
- Example Usage.

```python
from Pi20English import simplifiedPiCam
from time import sleep

camera = simplifiedPiCam()
camera.readValues()
sleep(1)

while True:
	camera.showSquare()
```
The example above makes another simplifiedPiCam object, starts taking values through the ``` readValues()``` method and returns the raw output of the camera to the display using the  ``` showSquare()``` method in a while loop.

The camre object has a pre set resolution of 640x480. If you want to change the resolution, you can do so like this:

``` camera = simplifiedPiCam(resolution=(1280, 720))```

If you want to see your code in a different window you can use the ```showSquare()``` method multiple times to make more threads. You can take the code below as a reference.
```python
from Pi20English import simplifiedPiCam
import imutils
import cv2
from time import sleep

camera = simplifiedPiCam()
camera.startReadingValues()
sleep(1)

while True:
	camera.showSquare()
	resized = imutils.resize(camera.readValues(), width=300)
	camera.showSquare("resized", resized)
	gray = cv2.cvtColor(camera.readValues(), cv2.COLOR_BGR2GRAY)
	camera.showSquare("black - gray", gray)
```
Controller
-
- Methods

```python
__refresh__()
```
Refreshes the values taken from the controller.  Calling it in the main thread **Is not reccomended** since it will most likely get stuck on that line.

```python
startTakingInputs()
```
Calls the ```__yenile__()``` method on a new thread so that the main thread can be used.

```python
readLeftValues()
```
Takes input from the left side of the joystick, and returns them as x, y float values.

```python
readRightValues()
```
Takes input from the left side of the joystick, and returns them as x, y float values.

```python
readButtons()
```
returns all button presses as an integer value in an array.

```python
readValues()
```
returns all values from the controller as a tuple ```(python readLeftValues(), python readRightValues(), python readButtons())```

- Example Usage

```python
import Pi20English

joystick = Pi20English.Controller()
joystick.startTakingInputs()

while True:
	lx, ly = joystick.readLeftValues()
	rx, ry = joystick.readRightValues()
	buttons = joystick.readButtons()

	print("Right joystick values: ", lx, ly)
	print("Left joystick values: ", rx, ry)

	if(0 in buttons):
		print("0 Buttons pressed!")
```
The code above reads the input of the joysticks and prints them out continuously. Don't forget that the ```startTakingInputs()``` method is required to be called so that you can take the values.

MotorControl
-
- Methods

```python
adjustSpeed(rightSpeed, leftSpeed)
```
Sets the sped of the motors using the pololu-drv-8835 library. The speeds range from -480 to +480(480 is the max backwards and forwards speed). The right and left speeds represent the right and left motors on the motor controller.

```python
changeControllerValueToMotorValue(x, y)
```
Gives motor speed values based on the joystick inputs. The x and y represents the joystick inputs and holds a value between 0 and 1.

- Example Usage

```python
import Pi20English
motors = Pi20English.MotorControl()

while True:
	motors.adjustSpeed(480, 480)
```
This code runs the motors forwards at max speed.

- Controller Example Usage

```python
import Pi20English

motors = Pi20English.MotorControl()

joystick = Pi20English.Controller()
joystick.startTakingInputs()

while True:
	lx, ly = joystick.readLeftValues()
	rightSpeed, leftSpeed = motors.changeControllerValueToMotorValue(lx, ly)

	motors.adjustSpeed(rightSpeed, leftSpeed)
```
The code above starts the controller and motor objects and enters a while loop. in the loop the  ```changeControllerValueToMotorValue()``` method is used to find the speed value of the motors.

ServoControl
-
- Methods

```python
setToContinuousSpin()
setToSingleSpin()
```
Sets servo state to either continous or single spin. The continuous spin dynamically keeps adjusting the angle of the servo, while the single spin is used to set an angle once and puts it in sleep mode.

```python
setAngle(angle)
```
Sets the servos postition based on an angle. If the state is set to single spin, then the a new thread will be made so that the servo will stop doing its current actions and sleep.

- Example Usage

Continuous Spin:
```python
import Pi20English
from time import sleep

servo = Pi20English.ServoControl(35)
servo.setToContinuousSpin()

angle = 0
add = 0

while True:
	servo.setAngle(angle)

	if(angle == 180):
		add = -1
	elif(angle == 0):
		add = 1
	angle += add
	sleep(0.05)
```
In the code above the servo is set to spin continuously, and a while loop is used to increase the servos angle one by one.

Single Spin:
```python
import Pi20English
from time import sleep

servo = Pi20English.ServoControl(35)
servo.setToSingleSpin()

while True:
	servo.setAngle(180)
	sleep(1)
	servo.setAngle(0)
	sleep(1)
```
In this code the servo is set to single spin, so the angle will be set to either 180 or 0 in 1 second intervals.

UltrasonicSensor
-
- Methods

```python
readDistance()
```
Returns the sensors recorded value.

- Example Usage

```python
import Pi20English

ultra = Pi20English.UltrasonicSensor(38, 40)
ultra.startMeasuringDistance()
while True:
	currentValue = ultra.readDistance()
	print(currentValue)
```
The code above prints the current distance recorded by the sensor. The paramaters given in the constructor are the pins of the sensor, being echo and trig respectively.


## License
[MIT](https://choosealicense.com/licenses/mit/)

